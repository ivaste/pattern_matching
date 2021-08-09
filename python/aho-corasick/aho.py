"""
•	Build a trie with the patterns.
•	Add suffix links for each node: BFS, for each node follow the father till the root to find the node that is the longest suffix.
•	Linear scan trough the text: starting from the root, if the current letter is in the children of the current node, go to that child, otherwise follow the suffix link and retry the letter.
•	If some patterns are substring of other ones, we have to Add dictionary links: for each node follow the failure links to the root, if there is a word node add a dictionary link between these two nodes, otherwise the node won’t have a dictionary link, stop at the first word node you encounter.
•	Linear scan trough the text: starting from the root, if the current letter is in the children of the current node, go to that child, otherwise follow the suffix link and retry the letter. If the current node is a word node, mark this word as found, if this node has a dictionary link follow the link and mark the word node, continue until you end up in node with no dictionary links, but for the next letter continue from the initial node.


"""


class node:
  def __init__(self,val=None,parent=None,end=False,word=None) -> None:
    self.val=val        #value
    self.parent=parent  #None means is the root
    self.end=end        #Is this node the END of a word?
    self.children={}    #maps val-->node
    self.suffix_link=None
    self.dict_link=None
    self.word=word      #Word associated with this node (only if the node is a word node)

patterns=["AAT","ATCG","C","CGC","G","GCA","GG","GGG","GTA"]
text="AATCGCAGAAAAGGG"
#Should find AAT,ATCG,C,CGC,G,GCA,GG,GGG (all except GTA)

#Build the trie from the patterns
trie=node()
for p in patterns:
  n=trie
  for c in p:
    if c not in n.children:
      new_node=node(val=c,parent=n)
      n.children[c]=new_node
    n=n.children[c]
  n.end=True
  n.word=p

#Add SUFFIX links to each node
root=trie
root.suffix_link=root
stack=[root]
while stack:
  n=stack.pop()
  suf=n.parent  #suffix
  pre=trie      #prefix
  while suf.val==pre.val:
    continue
#TODO...

#Try a linear scan with the trie without dictionary links
#TODO...

#Add DICTIONARY links
#TODO...

#Linear scan
#TODO...
