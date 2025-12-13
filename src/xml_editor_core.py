"""XMLEditor handles following functionalities for a given XML File
    1. Checks consistency and correctness of XML file
    2. Corrects errors in XML File
    
    3. Formats/Prettifies XML by adjusting indentations
    4. Reduces physical size of XML file by deleting whitespaces and indentations

    
    5. Converts XML file to JSON file

    6. Compresses XML File
    7. Decompresses XML File
    
    
"""
import json
from xml_tree import XNode, XTree

class XMLEditor:
    def __init__(self,filePath : str, xmlPastedFile = None) -> None:
        self.tree = XTree(filePath)
        self.jsonDictionary = {}
        self.filePath = filePath          
    
    def verify(self):
        """Checks consistency and correctness of XML file"""
        print("Checking Verified")
        
    def correct(self):
        """Corrects errors in XML File"""
    
    
    def format(self):
        """Formats/Prettifies XML by adjusting indentations"""
        
    def convert(self, root : XNode):
        """Converts XML file to JSON file"""

        if(not root):
            return
        if(not root.children):
            return {root.tag : root.text}
        
        jsonDictionary = {}
        for child in root.children:
            if child.tag in jsonDictionary:
                if type(jsonDictionary[child.tag]) != list:
                    jsonDictionary[child.tag] = [jsonDictionary[child.tag]]
                jsonDictionary[child.tag].append(self.convert(child))
            else:
                jsonDictionary.update(self.convert(child))
        # print(root.tag)
            
        return {root.tag : jsonDictionary}
        
    def minify(self):
        """Reduces physical size of XML file by deleting whitespaces and indentations"""
        
    def compress(self):
        """Compresses XML File"""
        
    def decompress(self):
        """Decompresses XML File"""
        
def main():
    editor = XMLEditor("src/sample.xml")
    tree = editor.tree
    root = tree.root
    jsonDict = editor.convert(root)
    prettyJsonDict = json.dumps(jsonDict, indent=4)
    print(prettyJsonDict)
    
if __name__ == "__main__":
    main()
    
        
    
    
        
    
