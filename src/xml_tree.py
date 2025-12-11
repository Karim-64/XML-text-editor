"""XML is a hierarchical data format, and the most natural way
to represent it is with a tree. We made two classes for this purpose
1. XTree represents the whole XML document as a tree
2. XNode represents a single node in this tree. 

Interactions with the whole document (reading and writing to/from files) are
done on the XTree level.
Interactions with a single XML element and its sub-element are
done on the XNode level.
"""
from __future__ import annotations

class XNode:
    def __init__(self, tag, text=""):
        self.tag = tag       
        self.text = text.strip() 
        self.children = []    
        self.parent = None 

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class XTree:
    """
    Class that handles all operations on XML files as a custom Tree structure
    """
    def __init__(self, root: XNode, file_path: str):
        # self.parse_xml(file_path)
        self.root = XNode
    
    
    def __parse(self, filePath : str) -> XTree | None:
        """Parses XML file into an XTree
        
        Args:
            filePath(str) : relative file path to .xml file
        Returns:
            XTree : A custom Tree structure that represents XML File using XNodes.
            
        """
        file = open(f"{file_path}", 'r')
        xml_string = file.read()

        xml_string = xml_string.strip()
        i = 0
        n = len(xml_string)
        stack = []
        root = None

        while i < n:
            if xml_string[i] == "<":
                j = xml_string.find(">", i)
                tag_content = xml_string[i + 1:j].strip()

                if tag_content.startswith("/"):
                    stack.pop()
                else:
                    node = XNode(tag_content)
                    if stack:
                        stack[-1].add_child(node)
                    else:
                        root = node
                    stack.append(node)

                i = j + 1
            else:
                j = xml_string.find("<", i)
                text_content = xml_string[i:j].strip()
                if text_content and stack:
                    stack[-1].text += text_content
                i = j
        return root
        
    
    def write(self, filePath : str, tree : XTree) -> None:
        """Creates new XML file from an XTree
        
        Args:
            filePath(str): relative file path to write .xml file
            tree(XTree): An XTree object that will produce the .xml file
        Returns:
            None
        """
        return
    