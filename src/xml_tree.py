"""
XML is a hierarchical data format, and the most natural way
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
    """
    Class that represents a single node in the XTree
    """

class XTree:
    """
    Class that handles all operations on XML files as a custom Tree structure
    """
    def __init__(self, filePath = None) -> None:
        pass
    
    def __parse(self, filePath : str) -> XTree | None:
        """Parses XML file into an XTree
        
        Args:
            filePath(str) : relative file path to .xml file
        Returns:
            XTree : A custom Tree structure that represents XML File using XNodes.
            
        """
        return
    
    def write(self, filePath : str, tree : XTree) -> None:
        """
        Creates new XML file from an XTree
        
        Args:
            filePath(str): relative file path to write .xml file
            tree(XTree): An XTree object that will produce the .xml file
        Returns:
            None
        """
        return
    