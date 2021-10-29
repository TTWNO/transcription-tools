from bs4 import BeautifulSoup as BS

"""
tree = [
  ("s", [
    ("a", [("b", [])]),
    ("d", []),
    ("c", [
      ("e",
        [
          ("f", [("h", [])]),
          ("g", [("i", [])]),
        ]
    )],
  )])
]
"""
"""
tree = [
  ("z (root, anscestor of a)", [
    ("y", [("x (leaf)", []), ("w (leaf)", [])]),
    ("v (anscestor of a)", [("u (leaf)", [])]),
    ("t (anscestor of a, parent of a)",
      [("s (sibling of a, leaf)", []), ("r (sibling of a, leaf)", []), ("a (descendant of a, anscestor of a)", [
      ("q (child of a, desandant of a)", [
        ("o (decendant of a, leaf)", []),
        ("n (decendant of a, leaf)", []),
        ("m (decendant of a, leaf)", []),
      ]),
      ("p (child of a, desendant of a, leaf)" , [])
    ])]),
  ])
]
"""
"""
tree = [
  ("4 (depth 0)", [
    ("1 (depth 1)", [
      ("0 (depth 2)", []),
      ("0 (depth 2)", []),
    ]),
    ("3 (depth 1)", [
      ("2 (depth 2)", [
        ("1 (depth 3)", [
          ("0 (depth 4)", []),
        ]),
        ("0 (depth 3)", []),
      ]),
      ("0 (depth 2)", []),
    ]),
  ])
]
"""
'''
tree = [
  ("no name", [
    ("1", [
      ("1", []),
      ("2", []),
    ]),
    ("2", []),
    ("3", [
      ("1", []),
      ("2", []),
      ("3", []),
    ]),
  ])
]
'''

'''
tree = [
  ("z", [
    ("v (subtree rooted at v)", [
      ("y (subtree rooted at v, left subtree of v)", [
        ("v (subtree rooted at v, left subtree of v", []),
        ("u (subtree rooted at v, left subtree of v", []),
      ]),
      ("x (subtree rooted at v, right subtree of v)", [
        ("w (subtree rooted at v, right subtree of v)", []),
      ]),
    ]),
    ("a", [("b", []), ("c", [])]),
  ])
]
'''

'''
tree = [
  ("v (3)", [
    ("a (2)", [
      ("e (1)", [
        ("g (0)", []),
        ("h (0)", []),
      ]),
      ("f (1)", [
        ("i (0)", []),
      ]),
    ]),
    ("b (1)", [
      ("c (0)", []),
      ("d (0)", []),
    ]),
  ])
]
'''

'''
tree = [
  ("A", [
    ("B", [
      ("D", []),
      ("E", []),
    ]),
    ("C", [
      ("F", []),
    ]),
  ])
]
'''

'''
tree = [
  ("5", [("3", []), ("6", [])])
]
tree = [
  ("5", [
    ("3", [
      ("2", []),
      ("6", []),
    ]),
    ("8", []),
  ])
]

tree = [
  ("5", [
    ("10 (right)", [
      ("20 (right)", [
        ("30 (right)", [
          ("25 (left)", []),
        ])
      ]),
    ]),
  ])
]

tree = [
  ("5", [])
]

tree = [
  ("500", [
    ("200", [
      ("100", []),
      ("300", [
        ("250", []),
        ("350", []),
      ]),
    ]),
    ("700", [
      ("600", [
        ("650 (keys in this subtree would be >600 , <700)", []),
        ("560", []),
      ]),
      ("800", []),
    ]),
  ])
]
'''

'''
tree = [
  ("3", [
    ("2", []),
    ("8", [
      ("5", [
        ("4", []),
        ("6", [
          ("7 (right)", []),
        ]),
      ]),
      ("9", []),
    ]),
  ])
]
'''

'''
tree = [
  ("5", [
    ("8 (right)", [
      ("10 (right)", []),
    ]),
  ])
]
'''

'''
tree = [
  ("5", [
    ("2", [
      ("1", []),
      ("3", []),
    ]),
    ("7", [
      ("6", []),
      ("8", []),
    ]),
  ])
]
'''

'''
tree = [
  ("1", [
    ("2 (right)", [
      ("3 (right)", [
        ("4 (right)", [
          ("5 (right)", [
            ("6 (right)", [
              ("7 (right)", [
                ("8 (right)", []),
              ]),
            ]),
          ]),
        ]),
      ]),
    ]),
  ])
]
'''

tree = [
  ("5", [
    ("3", [
      ("2 (left)", []),
    ]),
    ("8", [
      ("7", []),
      ("9", []),
    ]),
  ]),
]

'''
tree = [
  ("5", [
    ("3", [
      ("1 (left)", []),
    ]),
    ("10", []),
  ])
]
'''

'''
tree = [
  ("5", [
    ("1", []),
    ("10", [])
  ]),
]
'''

#tree = [("1", [])]

'''
tree = [
  ("4", [
    ("2", []),
    ("10", [
      ("7 (left)", [
        ("6", [
          ("5 (left)", []),
        ]),
        ("8", []),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("4", [
    ("2", []),
      ("7", [
        ("6", [
          ("5 (left", []),
        ]),
        ("8", []),
      ]),
  ]),
]
'''

'''
tree = [
  ("20", [
    ("6", [
      ("2", []),
      ("10", [
        ("7", [
          ("8 (right)", []),
        ]),
        ("12", []),
      ]),
    ]),
    ("...", []),
  ]),
]
'''

'''
tree = [
  ("30", [
    ("2", [
      ("1", []),
      ("6", [
        ("...", []),
        ("14", [
          ("11", [
            ("7", [
              ("9 (right)", [
                ("8", []),
                ("10", []),
              ]),
            ]),
            ("12", []),
          ]),
          ("...", []),
        ]),
      ]),
    ]),
    ("...", []),
  ])
]
'''

'''
tree = [
  ("30", [
    ("2", [
      ("1", []),
      ("7", [
        ("...", []),
        ("14", [
          ("11", [
            ("9", [
              ("8", []),
              ("10", []),
            ]),
            ("12", []),
          ]),
          ("...", []),
        ]),
      ]),
    ]),
    ("...", []),
  ]),
]
'''

'''
tree = [
  ("node", [
    ("node", [
      ("node", []),
      ("node", []),
    ]),
    ("node", [
      ("node", []),
      ("node", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("node", [
    ("node", [
      ("node", [
        ("...", [
          ("node", [
            ("node", [
            ]),
          ]),
        ]),
      ]),
    ])
  ]),
]
'''

'''
tree = [
  ("node", [
    ("node", [
      ("node", [
        ("node", []),
        ("node", []),
      ]),
      ("node", [
        ("node", []),
        ("node", []),
      ]),
    ]),
    ("node", [
      ("node", [
        ("node (right)", []),
      ]),
      ("node", [
        ("node", []),
        ("node", []),
      ]),
    ]),
  ])
]
'''

'''
tree = [
  ("node", [
    ("node (right)", [
      ("node (right)", [
        ("node (right)", [
          ("node (right)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("1", [
    ("2", []),
    ("2", []),
  ]),
]
'''

'''
tree = [
  ("5", [
    ("3", [
      ("2", []),
      ("4", []),
    ]),
    ("7", [
      ("6 (left)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("4", [
    ("2", [
      ("1", []),
      ("3", []),
    ]),
    ("6", [
      ("5", []),
      ("7", []),
    ]),
  ]),
]
'''

"""
tree = [
  ("root node", [
    ("left subtree (7 nodes)", [
      ("node", [
        ("node", [
          ("node (left)", []),
        ]),
        ("node", []),
      ]),
      ("node", [
        ("node (left)", []),
      ]),
    ]),
    ("right subtree (31 nodes)", [
      ("node", [
        ("node", [
          ("node", [
            ("node", []),
            ("node", []),
          ]),
          ("node", [
            ("node", []),
            ("node", []),
          ]),
        ]),
        ("node", [
          ("node", [
            ("node", []),
            ("node", []),
          ]),
          ("node", [
            ("node", []),
            ("node", []),
          ]),
        ]),
      ]),
      ("node", [
        ("node", [
          ("node", [
            ("node", []),
            ("node", []),
          ]),
          ("node", [
            ("node", []),
            ("node", []),
          ]),
        ]),
        ("node", [
          ("node", [
            ("node", []),
            ("node", []),
          ]),
          ("node", [
            ("node", []),
            ("node", []),
          ]),
        ]),
      ]),
    ]),
  ]),
]
"""

tree = [
  ("5", [
    ("3", [
      ("1", []),
      ("4", []),
    ]),
    ("7", [
      ("6", []),
      ("8", []),
    ]),
  ]),
]

tree = [
  ("3", [
    ("1", []),
    ("5", [
      ("4", []),
      ("7", [
        ("6", []),
        ("8", []),
      ]),
    ]),
  ]),
]

'''
tree = [
  ("v (root; h=k)", [
    ("u (h=k-1)", [
      ("left left (h=k-1)", [
        ("T1 (h=h-2)", [
          ("w", []),
        ]),
      ]),
      ("T2 (h=k-2)", []),
    ]),
    ("T3 (h=k-2)", []),
  ]),
]
'''

'''
tree = [
  ("root", [
    ("left", [
      ("...", []),
    ]),
    ("right", [
      ("right left", [
        ("...", [
          ("w", []),
        ]),
      ]),
      ("right right", [
        ("...", []),
      ]),
    ]),
  ]),
]
'''
'''
tree = [
  ("v", [
    ("left", [
      ("left left", [
        ("...", []),
      ]),
      ("left right", [
        ("...", [
          ("w\\*", []),
        ]),
      ]),
    ]),
    ("right", [
      ("...", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("v (root)", [
    ("T1 (left; h=k-2)", []),
    ("node (right; h=k)", [
      ("T2 (right left; h=k-2)", [
        ("w", []),
      ]),
      ("T3 (right right)", [
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("v (h=k)", [
    ("u (h=k-1)", [
      ("T1 (h=k-2)", []),
      ("w (h=k-2)", [
        ("T2 (h=k-3)", [
          ("Insertion here or... one other place", []),
        ]),
        ("T3 (h=k-3)", [
          ("Other possible insertion place.", []),
        ]),
      ]),
    ]),
    ("T4 (h=k-2)", []),
  ]),
]
'''

'''
tree = [
  ("a", [
    ("c (h=k)", [
      ("b", [
        ("T1", []),
        ("T2", [
          ("possible insertion", []),
        ]),
      ]),
      ("T3 (h=k-3)", [("possible insertion (not part of height)", [])]),
    ]),
    ("T4 (h=k-2)", []),
  ]),
]
'''

'''
tree = [
  ("c", [
    ("b (h=k-1)", [
      ("T1 (h=k-2)", []),
      ("T2 (h=k-2)", [
        ("possible insertion point", []),
      ]),
    ]),
    ("a (h=k-1)", [
      ("T3 (h=k-2)", [
        ("possible insertion", []),
      ]),
      ("T4 (h=k-2)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("X1", [
    ("...", []),
    ("node", [
      ("p (left)", [
        ("X2 (arrow to X1)", [
          ("... (right)", []),
        ]),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("root", [
    ("... (g; green)", [
      ("... (r; red)", [
        ("continues on with no detail", []),
        ("o (orange)", [
          ("continues on with no detail", []),
          ("node", [
            ("b (blue; left)", [
              ("continues on with no detail", []),
              ("continues oN with no detail", []),
            ]),
          ]),
        ]),
      ]),
      ("continues on with no detail", []),
    ]),
    ("continues on with no detail", []),
  ]),
]
'''

'''
tree = [
  ("node", [
    ("node", [
      ("...", []),
      ("...", [
        ("5 (left)", []),
      ]),
    ]),
    ("...", [
      ("14 (right; deleted)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("1", [
    ("2", [
      ("4", [
        ("8", []),
        ("9", []),
      ]),
      ("5", [
        ("10", []),
        ("11", []),
      ]),
    ]),
    ("3", [
      ("6", [
        ("12", []),
        ("13", []),
      ]),
      ("7", [
        ("14", []),
        ("15", []),
      ]),
    ]),
  ]),
]
'''

'''
tree = [
  ("1", [
    ("2", [
      ("4", [
        ("8", [
          "14", "15"
        ]),
        "9"
      ]),
      ("5", [
        ("10 (left)", [
          ("16 (left)", [
            "20", "21"
          ]),
        ]),
      ]),
    ]),
    ("3", [
      ("6", [
        ("11", [
          "17", ("18", ["22 (right)"])
        ]),
        "12"
      ]),
      ("7", [("13 (right)", ["19"])]),
    ]),
  ]),
]
'''

'''
tree = [
  ("root", [
    "child (right)"
  ]),
]
'''

'''
tree = [
  ("root", [
    ("child", [
      ("grandchild", [
        ("great granchild", []), 
        ("great granchild", []), 
]),
      ("grandchild", [
        ("great granchild", []), 
        ("great granchild", []), 
      ]),
    ]),
    ("child", [
      ("grandchild", [
        ("great granchild", []), 
        ("great granchild", []), 
      ]),
      ("grandchild", [
        ("great granchild", []), 
        ("great granchild", []), 
]),
    ])
  ])
]
'''

'''
tree = [
  ("...", [
    ("node at arbitrary depth", [
      "child node",
      "child node"
    ]),
    ("node at arbitrary depth", [
      "child node",
      "child node"
    ]),
    ("node at arbitrary depth", [
      "child node",
      "child node",
    ]),
    ("node at arbitrary depth", [
      "child node (left)"
    ]),
  ]),
]
'''

'''
tree = [
  ("1", [
    ("3 (highlighted arrow to 2)", [
      ("2", [
        ("7", []),
      ]),
      ("9", []),
    ]),
    ("6 (highlighted connection to 5)", [
      ("5", []),
      ("8", []),
    ]),
  ])
]
'''

'''
tree = [
  ("root (complete tree)", [
    ("... (anbiguous number of node/depth)", [
      ("10", [
        ("12", ["..."]),
        ("20", ["..."])
      ])
    ]),
    ("... (anbiguous number of node/depth)", [
      ("11", [
        ("13", ["..."]), 
        ("19", ["..."]),
      ])
    ]),
  ]),
]
'''

'''
tree = [
  ("root", [
    ("child", [
      ("grandchild", [
        "great grandchild",
        "great grandchild",
      ]),
      ("grandchild", [
        "great grandchild",
        "great grandchild",
      ]),
    ]),
    ("child", [
      ("grandchild", [
        "inserted node"
      ]),
      ("grandchild", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("1", [
    ("2", [
      "..."
    ]),
    ("3", [
      ("6", [
        ("10 (left)", []),
      ]),
      ("8", []),
    ]),
  ])
]
'''

'''
tree = [
  ("?", [
    ("7", [
      ("10", []),
      ("12", []),
    ]),
    ("6 (arrow towards root)", [
    ]),
  ]),
]
'''

'''
tree = [
  ("2", [
    ("4", [
      ("7", []),
      ("8", []),
    ]),
    ("3", [
      ("5 (left)", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("0", [
    ("1", [
      ("3", [
        ("7", []),
        ("8", []),
      ]),
      ("4", [
        ("9", []),
        ("10", []),
      ]),
    ]),
    ("2", [
      ("5", [
        ("11 (left)", []),
      ]),
      ("6", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("2", [
    ("7", [
      "8", "10"
    ]),
    ("6", [
      ("9", []),
      ("1", []),
    ]),
  ]),
]
'''

'''
tree = [
  ("1 (2 is crossed out, arrow to 2)", [
    ("7", [
      "8", "10"
    ]),
    ("2 (6 is crossed out, arrow to 6)", [
      "9", "6 (1 is crossed out)"
    ]),
  ]),
]
'''

'''
tree = [
  ("7", [
    ("8", [
      "11", "10"
    ]),
    ("9", [
    ]),
  ]),
]
'''

tree = [
  ("0", [
    ("1", [
      ("3", [
        ("7", [
          ("15", []),
          ("16", []),
        ]),
        ("8", [
          ("17", []),
          ("18", []),
        ]),
      ]),
      ("4", [
        ("9 (label: last internal node)", [
          ("19", []),
          ("20", []),
        ]),
        ("10", []),
      ]),
    ]),
    ("2", [
      ("5", [
        ("11", []),
        ("12", []),
      ]),
      ("6", [
        ("13", []),
        ("14", []),
      ]),
    ]),
  ]),
]

ID = "t8"

def _generate_tree(tup):
  html = ""
  html += "<li role=\"treeitem\" tabindex=\"-1\">"
  if type(tup) == str:
    html += "<span id=\"{1}_{2}\">{0}</span></li>".format(tup, ID, tup.split(" ")[0])
    return html
  html += "<span id=\"{1}_{2}\">{0}</span>".format(tup[0], ID, tup[0].split(" ")[0])
  if len(tup[1]) > 0:
    html += "<ul role=\"group\">"
    for i in tup[1]:
      html += _generate_tree(i)
    html += "</ul>"
  html += "</li>"
  return html

def generate_tree(treeobj):
  html = "<ul role=\"tree\">"
  html += _generate_tree(treeobj)
  html += "</ul>"
  return html

print("<!-- AUTO GENERATED FROM CUSTOM PYTHON CODE -->")
bs = BS(generate_tree(tree[0]), "html.parser")
print(bs.prettify())
print("<!-- END OF GENERATED CODE -->")
