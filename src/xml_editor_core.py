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
from collections import deque

def find_tag_in_stack(stack, target_tag_name):
    temp_stack = []
    found = False
    counter = -1

    while (not found and stack):
        temp = stack.pop()
        temp_stack.append(temp)
        counter = counter + 1

        if(temp[0] == target_tag_name):
            found = True

    while temp_stack:
        stack.append(temp_stack.pop())

    return (found, counter)


def log_error(errors, error_type, tag, line, message):
    # Recording the errors in a list of dicts
    # while each dict contains a single error
    errors.append(
        {
            "type": error_type,
            "tag": tag,
            "line": line,
            "message": message
        }
    )



class XMLEditor:
    def __init__(self,filePath : str, xmlPastedFile = None) -> None:
        self.filePath = filePath
        self.tree = XTree(filePath)
        self.jsonDictionary = {}
        self.filePath = filePath          
    
    def verify(self, output_file : str = None):
        """
        Checks consistency and Correcting of XML file
        1-  Every opening tag has a matching closing tag.
        2-  Elements are properly nested.
        3-  There is a single root elements
        4-  Special characters are correctly escaped < for example
        """
        with open(self.filePath, "r") as input_file:
            xml_content = input_file.read()

        xml_content = xml_content.strip()
        xml_queue = deque() 
        errors = []
        current_index = 0
        current_line = 1    
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
                        if tag_name == tag_stack[-1][0]: 
                            xml_queue.append(f"</{tag_name}>")
                            tag_stack.pop()
                        else:
                            found, number_of_missing_closing_tags = find_tag_in_stack(tag_stack, tag_name)

                            if found:
                                # Missing closing tags above the correct one
                                for i in range(number_of_missing_closing_tags):
                                    open_tag, open_line = tag_stack.pop()
                                    log_error(
                                        errors,
                                        "MissingClosingTag",
                                        open_tag,
                                        open_line,
                                        f"Missing closing tag for <{open_tag}>"
                                    )
                                    xml_queue.append(f"</{open_tag}>")
                            else:
                                # Truly incorrect closing tag (typo) 
                                log_error(
                                    errors,
                                    "IncorrectClosingTag",
                                    tag_name,
                                    current_line,
                                    f"Incorrect closing tag </{tag_name}>"
                                )
                                # Fix by closing the top element
                                xml_queue.append(f"</{tag_stack[-1][0]}>")
                                tag_stack.pop()
                                current_index = closing_bracket_index + 1
                                continue

                            xml_queue.append(f"</{tag_name}>")
                            tag_stack.pop()

                # Opening tags handling
                else:
                    if current_index and not tag_stack:
                        log_error(
                            errors,
                            "MultipleRoots",
                            None,
                            current_line,
                            "Multiple root elements detected"
                        )
                        break
                    tag_stack.append((tag_internal_text, current_line))  
                    xml_queue.append(f"<{tag_internal_text}>")
                
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
                    else:
                        log_error(
                            errors,
                            "IllegalCharacter",
                            None,
                            current_line,
                            "Illegal '<' character detected in text"
                        )
                        next_opening_bracket_index = xml_content.find("<", next_char_index)

                # checking for illegal '>'
                check_index = current_index
                while check_index < (next_opening_bracket_index if next_opening_bracket_index != -1 else total_length):
                    if xml_content[check_index] == '>':
                        log_error(
                            errors,
                            "IllegalCharacter",
                            None,
                            current_line + xml_content[current_index:check_index].count('\n'),
                            "Illegal '>' character detected in text"
                        )
                    check_index += 1
                
                text_content = xml_content[current_index : next_opening_bracket_index]
                cleaned_text = text_content.strip()
                
                if cleaned_text:
                    xml_queue.append(cleaned_text)

                for char in xml_content[current_index : next_opening_bracket_index]:
                    if char not in ('\n', ' '):
                        is_leaf = True
                        break

                if is_leaf:
                    if next_opening_bracket_index != -1 and xml_content[next_opening_bracket_index + 1] != '/':
                        open_tag, open_line = tag_stack.pop()
                        log_error(
                            errors,
                            "MissingClosingTag",
                            open_tag,
                            open_line,
                            f"Missing closing tag for <{open_tag}>"
                        )
                        xml_queue.append(f"</{open_tag}>")
                    is_leaf = False

                if next_opening_bracket_index != -1:
                    current_line += xml_content.count('\n', current_index, next_opening_bracket_index)
                else:
                    current_line += xml_content.count('\n', current_index, total_length)

                current_index = next_opening_bracket_index

        # Checking for tags without closing 
        while tag_stack:
            open_tag, open_line = tag_stack.pop()
            log_error(
                errors,
                "MissingClosingTag",
                open_tag,
                open_line,
                f"Missing closing tag for <{open_tag}> at end of file"
            )
            xml_queue.append(f"</{open_tag}>")


        print("\nVerification Report:")
        for err in errors:
            print(f"[{err['type']}] Line {err['line']}: {err['message']}")

        print(f"\nTotal errors found: {len(errors)}")

        # Write the output into a file
        if output_file:
            with open(output_file, "w") as f:
                i = 0
                queue_list = list(xml_queue)
                
                while i < len(xml_queue):
                    item = queue_list[i]
                    f.write(item + '\n')
                    i += 1
            
    def correct(self):
        """Corrects errors in XML File"""
    
    def convert(self, root : XNode | None, siblingFlag = False):
        """Converts XML file to JSON file"""

        if(not root):
            raise TypeError
        if(not root.children):
            if(siblingFlag): 
                return root.text
            return {root.tag : root.text}
        
        jsonDictionary = {}
        for i,child in enumerate(root.children):       
            if child.tag in jsonDictionary:
                if type(jsonDictionary[child.tag]) != list:
                    jsonDictionary[child.tag] = [jsonDictionary[child.tag]]
                (jsonDictionary[child.tag]).append((self.convert(child, True)))
            else:
                jsonDictionary.update(self.convert(child, False)) # pyright: ignore[reportArgumentType, reportCallIssue]
                
        if(siblingFlag):
            return jsonDictionary
        else:
            return {root.tag : jsonDictionary}
          
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
      
    def minify(self):
        """Reduces physical size of XML file by deleting whitespaces and indentations"""
        
    def compress(self):
        """Compresses XML File"""
        
    def decompress(self):
        """Decompresses XML File"""
