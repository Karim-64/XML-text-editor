"""
    XMLEditor handles following functionalities for a given XML File
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
        self.filePath = filePath
        self.tree = XTree(filePath)
    
    def verify(self):
        """
        Checks consistency and correctness of XML file
        1-  Every opening tag has a matching closing tag.
        2-  Elements are properly nested.
        3-  There is a single root elements
        4-  Special characters are correctly escaped < for example

        to do:
        1-  Every Error should be kept and continue instead of break
        2-  We must store the line where the error occured 
        3-  We should be able to fix it as well
        """
        with open(self.filePath, "r") as input_file:
            xml_content = input_file.read()

        xml_content = xml_content.strip()
        current_index = 0
        current_line = 0    
        is_leaf = False
        total_length = len(xml_content)
        tag_stack = []

        while current_index < total_length:
            # First we need to handle the tags
            if xml_content[current_index] == "<":
                closing_bracket_index = xml_content.find(">", current_index)
                tag_internal_text = xml_content[current_index + 1 : closing_bracket_index].strip()

                # Closing tags handling
                # the same function should be called here 
                # to differentiate between the mismatch and incorrect tag
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

            # Second Text handling
            else:
                next_opening_bracket_index = xml_content.find("<", current_index)

                # Validation of the text
                while next_opening_bracket_index != -1:
                    next_char_index = next_opening_bracket_index + 1
                    next_char = xml_content[next_char_index]

                    # Valid tag start
                    if next_char.isalpha() or next_char == '/':
                        break

                    # Illegal '<'
                    else:
                        print("illegal '<' detected")
                        next_opening_bracket_index = xml_content.find("<", next_char_index)

                # Checking if the the tag is leaf or not  
                for char in xml_content[current_index : next_opening_bracket_index]:
                    if (char != '\n' and char != ' '):
                        is_leaf = True
                        break
                    
                # Handling leaf nodes closing terminals
                if is_leaf:
                    if xml_content[next_opening_bracket_index + 1] == '/':
                        closing_bracket_index = xml_content.find(">", next_opening_bracket_index + 1) 
                        tag_internal_text = xml_content[next_opening_bracket_index + 2 : closing_bracket_index]
                        if(tag_stack):
                            if(tag_internal_text != tag_stack[-1]):
                                # Should check on the contents of the stack to check if the
                                # current closing is a mismatch or wrong closing tag
                                # implementing a function to travesre the stack
                                # would make it better 
                                print(tag_stack[-1])
                                print(f"The closing of {tag_stack[-1]} is missing")
                    else:
                        print(f"The closing of {tag_stack[-1]} is missing")
                    tag_stack.pop()
                    is_leaf = False
                    next_opening_bracket_index = xml_content.find("<", closing_bracket_index) 

                    
                # Breaking the loop if we reached the end of file
                if next_opening_bracket_index == -1:
                    break

                current_index = next_opening_bracket_index

        # Checking for tags without closing 
        if tag_stack:
            print("error")

        print("Verification is finished")
            

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