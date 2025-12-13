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
        with open(self.filePath, "r") as file:
            xml_str = file.read()
            indent = 0
            output=""
            i=0
            n= len(xml_str)
            flag=0
            while i<n:
                if(xml_str[i]=="<"):
                    j= xml_str.find(">",i)
                    if j==-1:
                        break
                    tag=xml_str[i+1:j].strip()
                    if tag.startswith("/"):
                        if not flag:
                            indent -=1
                            output += "   "*indent +"<"+ tag+">"+"\n"
                            
                        else:
                            indent -=1
                            output= output.strip()+"<"+ tag+">"+"\n"
                            flag=0
                    elif tag.endswith("/"):
                        output += "   "*indent +"<"+ tag+">"+"\n"
                    else:
                        output += "   " * indent + "<"+ tag+">"+"\n"
                        indent += 1
                    i= j+1
                else:
                    j = xml_str.find("<", i)
                    if j == -1:
                        j = n
                    text = xml_str[i:j].strip()
                    if text:
                        if(len(text)<20 and  text.strip() != ""):
                            output =output.strip()+text.strip()
                            flag=1
                        else:
                            output += "   " * indent + text + "\n" 
                            flag=0
                    i = j
        with open("formatted_output.xml", "w") as file:
            file.write(output)
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
