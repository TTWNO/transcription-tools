# used if you want to add links to the tree, or a node in the tree
ID = "t0"

# example of tree (commented out)
'''
tree  = [
  ("root", [
    ("child", [
      "grandchild", "grandchild"
    ]),
    ("child", []),
  ]),
]
'''

# every node is written ("value", [])
# the list inside contains all children of that node
# a string can also be used (i.e. "grandchildren"), but it can have no children

# the tree you want converted to HTML, here:
tree = [
  ("n", [
    ("n-1", [
      ("n-2", [
        ("n-3", [
          ("... (left)", [
            "1", "0"
          ]),
        ]),
        "0"
      ]),
      "0"
    ]),
    "0"
  ]),
]
