"""
graph.py create an accessible graph
"""
import json
import sys
from bs4 import BeautifulSoup as bs

def original(graph):
  html = "<ul>"
  for x in graph:
    html += f"<li id=\"{x['short_name']}\">" + x["name"] + f": <a href=\"#from_{x['short_name']}\">from</a>, <a href=\"#to_{x['short_name']}\">to</a>"
    if "subitems" in x:
      html += "<ul>"
      for y in x["subitems"]:
        html += f"<li id=\"{y['short_name']}\">" + y["name"] + f": <a href=\"#from_{y['short_name']}\">from</a>, <a href=\"#to_{y['short_name']}\">to</a>" + "</li>"
      html += "</ul>"
    html += "</li>"
  html += "</ul>"
  return html

def flatten(graph):
  new = list()
  for n in graph:
    new.append(n)
    if "subitems" in n:
      for m in n["subitems"]:
        new.append(m)
  return new

def sntn(graph, short_name):
  for n in flatten(graph):
    if n["short_name"] == short_name:
      return n["name"]
  return None

def connections_to(graph):
  def _conns(node):
    html = f"<li id=\"to_{node['short_name']}\">" + f"<a href=\"#{node['short_name']}\">{node['name']}</a>"
    if "cons" in node:
      html += "<ul>"
      for c in node["cons"]:
        html += f"<li id=\"to_{node['short_name']}_from_{c}\">" + f"<a href=\"#{c}\">{sntn(graph, c)}</a>" + "</li>"
      html += "</ul>"
    html += "</li>"
    return html

  html = "<ul>"
  for n in flatten(graph):
    html += _conns(n)
  html += "</ul>"
  return html

def get_reverse_connections(sn, graph):
  cons = list()
  for n in flatten(graph):
    if "cons" in n and sn in n["cons"]:
      cons.append(n["short_name"])
  return cons

def connections_from(graph):
  def _conns(node):
    html = f"<li id=\"from_{node['short_name']}\">" + f"<a href=\"#{node['short_name']}\">{node['name']}</a>"
    html += "<ul>"
    for c in get_reverse_connections(node["short_name"], graph):
      html += f"<li id=\"from_{node['short_name']}_to_{c}\">" + f"<a href=\"#{c}\">{sntn(graph, c)}</a>" + "</li>"
    html += "</ul></li>"
    return html

  html = "<ul>"
  for n in flatten(graph):
    html += _conns(n)
  html += "</ul>"
  return html
  

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Must specify .json file")
    exit()
  f = open(sys.argv[1], "r")
  graph = json.loads(f.read())
  html = "<!DOCTYPE html><html><head><meta charset=\"utf-8\"></head><body>"
  html += "<h1>Graph</h1>"
  html += "<p>The ideal solution to this would actually be to turn the graph into a 3D braille model so it can be printed. Due to conditions of remoteness and the time required to do such a task though, this is not possible right now.</p>"
  html += "<p>Please do not navigate to connections manually. Use the links.</p>"
  html += "<h2>Nodes of Graph</h2>"
  html += original(graph)
  html += "<h2>Graph Connections (to)</h2>"
  html += connections_to(graph)
  html += "<h2>Graph Connections (form)</h2>"
  html += connections_from(graph)
  html += "</body></html>"
  soup = bs(html, "html.parser")
  print(soup.prettify())
