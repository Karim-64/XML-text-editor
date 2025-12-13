"""XMLEditor handles following functionalities for a given XML File
    1. Checks consistency and correctness of XML file
    2. Corrects errors in XML File
    3. Formats/Prettifies XML by adjusting indentations
    4. Converts XML file to JSON file
    5. Reduces physical size of XML file by deleting whitespaces and indentations
    6. Compresses XML File
    7. Decompresses XML File
    
    
"""
from xml_tree import XTree
from xml_tree import XNode

class XMLEditor:

    LUT = {}

    def __init__(self,filePath : str, xmlPastedFile = None) -> None:
        self.tree = XTree(filePath)
    
    def verify(self):
        """Checks consistency and correctness of XML file"""
        print("Checking Verified")
        
    def correct(self):
        """Corrects errors in XML File"""
    
    def format(self):
        """Formats/Prettifies XML by adjusting indentations"""
        
    def convert(self):
        """Converts XML file to JSON file"""
        
    def minify(self):
        """Reduces physical size of XML file by deleting whitespaces and indentations"""
        
    def compress(self, tree : XNode):
        """Compresses XML File"""
        compStack = []
        compStack.append(tree)
        while compStack:
            temp = compStack.pop()
            if temp.tag is not None and len(temp.tag) > 2:
                if temp.tag in self.LUT.values():
                    for key in self.LUT:
                        if self.LUT[key] == temp.tag:
                            temp.tag = key
                elif temp.tag[0] not in self.LUT:
                    self.LUT[temp.tag[0]] = temp.tag
                    temp.tag = temp.tag[0]
                elif (temp.tag[0] + temp.tag[-1]) not in self.LUT:
                    self.LUT[temp.tag[0] + temp.tag[-1]] = temp.tag
                    temp.tag = temp.tag[0] + temp.tag[-1]
                else:
                    self.LUT[temp.tag[0:1] + temp.tag[-1]] = temp.tag
                    temp.tag = temp.tag[0:1] + temp.tag[-1]
                # print(temp.tag)
            for child in temp.children:
                compStack.append(child)
        else:
            return

        
    def decompress(self):
        """Decompresses XML File"""