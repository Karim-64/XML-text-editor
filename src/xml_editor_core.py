"""
    XMLEditor handles following functionalities for a given XML File
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
        self.filePath = filePath
    
    def verify(self):
        """
        Checks consistency and correctness of XML file
        1-  Every opening tag has a matching closing tag.
        2-  Elements are properly nested.
        3-  There is a single root elements
        4-  Special characters are correctly escaped < for example
        """
        with open(self.filePath, "r") as input_file:
            xml_content = input_file.read()

        xml_content = xml_content.strip()
        current_index = 0
        total_length = len(xml_content)
        tag_stack = []

        while current_index < total_length:
            # First we need to handle the tags
            if xml_content[current_index] == "<":
                closing_bracket_index = xml_content.find(">", current_index)
                tag_internal_text = xml_content[current_index + 1 : closing_bracket_index].strip()

                # Closing tags handling
                if tag_internal_text.startswith("/"):
                    tag_name = tag_internal_text[1:]
                    if tag_stack:
                        if tag_name != tag_stack[-1]:
                            print(f"Error at {tag_stack[-1]}")
                            break
                        else:
                            tag_stack.pop()

                # Opening tags handling
                else:
                    if current_index and not tag_stack:
                        print("There can't be multiple roots")
                        break
                    tag_stack.append(tag_internal_text)
                    # print(tag_stack[-1])
                
                current_index = closing_bracket_index + 1

            # Text handling
            else:
                next_opening_bracket_index = xml_content.find("<", current_index)
                
                # Checking for illegal > in the text
                while next_opening_bracket_index != -1:
                    if next_opening_bracket_index + 1 < total_length:
                        if not (
                            xml_content[next_opening_bracket_index + 1].isalpha() 
                            or xml_content[next_opening_bracket_index + 1] in ["/"]
                        ):
                            next_opening_bracket_index = xml_content.find("<", next_opening_bracket_index + 1)
                        else:
                            break
                    else:
                        break

                if next_opening_bracket_index == -1:
                    break
                current_index = next_opening_bracket_index

        # checking for tags without closing 
        if tag_stack:
            print("error")

        print("Checking Verified")
            

    def correct(self):
        """Corrects errors in XML File"""
    
    
    def format(self) -> str:
        """Formats/Prettifies XML by adjusting indentations
        Returns:
            output(str) : formatted and prettified xml string.
        """
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
        return output

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
