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
import json

class XMLEditor:

    LUT = {}
    textIdDict = {}
    space_Enc = {}
    FILE = "compress_dicts.json"

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
    def decompress(filePath : str):
        """Decompresses XML File"""
        xml_str = Path(filePath).read_text(encoding="utf-8")

        # load dictionaries used in compression
        with open(XMLEditor.FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            XMLEditor.LUT = data["LUT"]
            XMLEditor.textIdDict = data["textIdDict"]
            XMLEditor.space_Enc = data["space_Enc"]

        for key, value in XMLEditor.space_Enc.items():
            xml_str = xml_str.replace(key, value)

        for key, value in XMLEditor.LUT.items():
            xml_str = xml_str.replace('<' + key + '>', '<' + value + '>')
            xml_str = xml_str.replace('</' + key + '>', '</' + value + '>')

        for key, value in XMLEditor.textIdDict.items():
            xml_str = xml_str.replace(key, value)
        
        return xml_str

    @staticmethod
    def compress(filePath : str):
        """Compresses XML File"""
        tree = XMLEditor(filePath).tree.root
        # txtId = 1
        char = '\u4E00'  # chinese letters start at 4E00 and end at 9FFF
        decimal_value = ord(char)
        stack = []
        stack.append(tree)
        while stack:
            temp = stack.pop()
            if temp.tag is not None:
                if temp.tag in XMLEditor.LUT.values():
                    for key in XMLEditor.LUT:
                        if XMLEditor.LUT[key] == temp.tag:
                            temp.tag = key
                elif temp.tag[0] not in XMLEditor.LUT.keys():
                    XMLEditor.LUT[temp.tag[0]] = temp.tag
                    temp.tag = temp.tag[0]
                elif (temp.tag[0] + temp.tag[-1]) not in XMLEditor.LUT.keys():
                    XMLEditor.LUT[temp.tag[0] + temp.tag[-1]] = temp.tag
                    temp.tag = temp.tag[0] + temp.tag[-1]
                else:
                    for i in range(1,len(temp.tag)-1):
                        if (temp.tag[0:i] + temp.tag[-1]) not in XMLEditor.LUT.keys():
                            XMLEditor.LUT[temp.tag[0:i] + temp.tag[-1]] = temp.tag
                            temp.tag = temp.tag[0:i] + temp.tag[-1]
                            break

            if temp.text:
                if temp.text in XMLEditor.textIdDict.values():
                    for key in XMLEditor.textIdDict:
                        if XMLEditor.textIdDict[key] == temp.text:
                            temp.text = key
                elif decimal_value <= 0x9FFF:
                    XMLEditor.textIdDict[chr(decimal_value)] = temp.text
                    temp.text = chr(decimal_value)
                    decimal_value +=1

            for child in temp.children:
                stack.append(child)
        else:
            file = open(f"{filePath}", 'r')
            xml_str = file.read()
            i = 0
            j = 0

            for key, value in XMLEditor.textIdDict.items():
                xml_str = xml_str.replace(value, key)

            for key, value in XMLEditor.LUT.items():
                xml_str = xml_str.replace(value, key)

            n = len(xml_str)

            while i < n and j < n:
                while i < n and xml_str[i] != " ":
                    i += 1
                if i >= n:
                    break
                j = i
                while j < n and xml_str[j] == " ":
                    j += 1
                # now i points to first space and j to first non-space character after it
                XMLEditor.space_Enc[str(j - i) + '&'] = xml_str[i:j]
                i = j

            items = list(XMLEditor.space_Enc.items())
            items.sort(key=lambda item: len(item[1]),
                       reverse=True)  # lambda is used instead of defining a method, item[0]=key,item[1]=value,reverse->Descending order
            XMLEditor.space_Enc = dict(items)

            for key, value in XMLEditor.space_Enc.items():
                xml_str = xml_str.replace(value, key)

            # COMPRESSION - DECOMPRESSION DICTIONARIES FILE
            # load old data if file exists / make a new file
            if Path(XMLEditor.FILE).exists():
                with open(XMLEditor.FILE, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError: # if the file exists but empty
                        data = {"LUT": {}, "textIdDict": {}, "space_Enc": {}}
            else:
                data = {
                    "LUT": {},
                    "textIdDict": {},
                    "space_Enc": {}
                }

            # merge dictionaries
            data["LUT"].update(XMLEditor.LUT)
            data["textIdDict"].update(XMLEditor.textIdDict)
            data["space_Enc"].update(XMLEditor.space_Enc)

            # write back with merged dictionaries
            with open(XMLEditor.FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
        return xml_str


def main():
    # XMLEditor.compress("sample.xml")
    # XMLEditor.decompress("sample.comp")
    pass

if __name__ == "__main__":
    main()