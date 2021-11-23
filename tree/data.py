# used if you want to add links to the tree, or a node in the tree
ID = "t9"

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
    ("n/2", [
      ("n/4", [
        ("n/8", [
          ("...", [
            ("2", [
              "1", "1"
            ]),
          ]),
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
    ]),
    ("n/2", [
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
      ("n/4", [
        ("n/8", [
          "..."
        ]),
        ("n/8", [
          "..."
        ]),
      ]),
    ]),
  ]),
]
