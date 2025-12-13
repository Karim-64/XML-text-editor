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

class XMLEditor:
    def __init__(self,filePath : str, xmlPastedFile = None) -> None:
        self.tree = XTree(None, filePath)
        self.filePath = filePath          
    
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
        
    def compress(self):
        """Compresses XML File"""
        
    def decompress(self):
        """Decompresses XML File"""



editor = XMLEditor("unprettified.xml")
editor.format()
