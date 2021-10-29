gid = "g12"
graph = {
  "a": ["b"],
  "b": ["a", "c"],
  "c": ["b", "d", "e", "s"],
  "d": ["c", "s"],
  "e": ["c", "g"],
  "f": ["h"],
  "g": ["e", "h", "t"],
  "h": ["f", "g", "t"],
  "s": ["c", "d"],
  "t": ["g", "h"],
}

print("node|connections")
print("---|---")
for node,vertexes in graph.items():
  print("<span id=\"{0}-{1}\">{1}</span>|{2}".format(gid, node, ",".join(["<a href=\"#{1}-{0}\">{0}</a>".format(v, gid) for v in vertexes])))
