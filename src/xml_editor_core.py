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
from pathlib import Path

class XMLEditor:

    LUT = {}
    textIdDict = {}
    space_Enc = {}

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

    @staticmethod   
    def compress( filePath : str):
        """Compresses XML File"""
        editor = XMLEditor(filePath)
        Editor_tree = editor.tree
        tree = Editor_tree.root

        txtId=1
        stack = []
        stack.append(tree)
        while stack:
            temp = stack.pop()
            # Logic
            if temp.tag is not None :
                if temp.tag in XMLEditor.LUT.values():
                    for key in XMLEditor.LUT:
                        if XMLEditor.LUT[key] == temp.tag:
                            temp.tag = key
                elif temp.tag[0] not in XMLEditor.LUT:
                    XMLEditor.LUT[temp.tag[0]] = temp.tag
                    temp.tag = temp.tag[0]
                elif (temp.tag[0] + temp.tag[-1]) not in XMLEditor.LUT:
                    XMLEditor.LUT[temp.tag[0] + temp.tag[-1]] = temp.tag
                    temp.tag = temp.tag[0] + temp.tag[-1]
                else:
                    XMLEditor.LUT[temp.tag[0:1] + temp.tag[-1]] = temp.tag
                    temp.tag = temp.tag[0:1] + temp.tag[-1]
            if temp.text !="":
                if temp.text in XMLEditor.textIdDict.values():
                    for key in XMLEditor.textIdDict:
                        if XMLEditor.textIdDict[key]==temp.text:
                            temp.text=key
                else:
                    XMLEditor.textIdDict[str(txtId)] = temp.text
                    temp.text = str(txtId)
                    txtId+=1


            for child in temp.children:
                stack.append(child)
        else:
            file = open(f"{filePath}", 'r')
            xml_str = file.read()
            i = 0
            j = 0

            for key,value in XMLEditor.textIdDict.items():
                xml_str=xml_str.replace(value,key)

            for key,value in XMLEditor.LUT.items():
                xml_str=xml_str.replace(value,key)

            n = len(xml_str)

            while i<n and j<n:
                while i<n and xml_str[i] != " ":
                    i+=1
                if i>=n:
                    break
                j=i
                while j<n and xml_str[j] == " ":
                    j+=1
                #now i points to first space and j to first non-space character after it
                XMLEditor.space_Enc[str(j-i)+'&']=xml_str[i:j]
                i=j


            items=list(XMLEditor.space_Enc.items())
            items.sort(key=lambda item: len(item[1]),reverse=True) #lambda is used instead of defining a method, item[0]=key,item[1]=value,reverse->Descending order
            for key,value in items:
                xml_str=xml_str.replace(value,key)

            Path.touch('output_file.comp')
            P=Path('output_file.comp')
            P.write_text(xml_str)

            return

        
    def decompress(self):
        """Decompresses XML File"""
