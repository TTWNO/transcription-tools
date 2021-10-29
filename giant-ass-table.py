from bs4 import BeautifulSoup as BS

table = list()

with open("table.csv", "r") as f:
  for row in f:
    fil = list()
    for cell in row.split(","):
      if cell[:2] == "$$":
        cell = cell.replace("$$", "")
        cell = "{% katex %}" + cell
        cell = cell + "{% endkatex %}"
      fil.append(cell)
    table.append(fil)

def generate_table(table):
  html = "<table><thead><tr>"
  html += "<th colspan=\"2\"></th>"
  html += "<th colspan=\"3\">Exponent</th>"
  html += "<th colspan=\"2\">Fraction</th>"
  html += "<th colspan=\"3\">Value</th>"
  html += "</tr><tr>"
  html += "<th>Description</th>"
  html += "<th>Bit Representation/th>"
  html += "<th>exp</th>"
  html += "<th>E</th>"
  html += "<th>{% katex %}2^{E}{% endkatex %}</th>"
  html += "<th>frac</th>"
  html += "<th>M</th>"
  html += "<th>{% katex %}M 2^{E}{% endkatex %}</th>"
  html += "<th>V</th>"
  html += "<th>Decimal</th>"
  html += "</tr></thead><tbody>"

  for row in table:
    html += "<tr>"
    for cell in row:
      html += "<td>" + cell + "</td>"
    html += "</tr>"

  html += "</tbody></table>"
  return html

print("<!-- AUTO GENERATED FROM CUSTOM PYTHON CODE -->")
bs = BS(generate_table(table), "html.parser")
print(bs.prettify())
print("<!-- END OF GENERATED CODE -->")
