import argparse
from xml_editor_core import XMLEditor

editor = XMLEditor("file.xml")
editor.verify()

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("command", help = "Choose a command", type=str
#                         ,choices = ["verify", "format", "json", "mini",
#                                     "compress", "decompress"])
#     parser.add_argument("-i", "--input", help="<file_name.xml>", type=str)
#     parser.add_argument("-f", "--fix", action="store_true")
#     parser.add_argument("-o", "--output", help="<file_name.xml>", type=str)
#     args = parser.parse_args()
    
#     #===================================================
#     # TODO: Parse file path from CLI like command
#     filePath : str = ""
#     editor : XMLEditor = XMLEditor(filePath)
#     #===================================================
    
#     if args.command == "verify":
#         editor.verify()
#     elif args.command == "format":
#         editor.format()
#     elif args.command == "json":
#         editor.convert()
#     elif args.command == "mini":
#         editor.minify()
#     elif args.command == "compress":
#         editor.compress()
#     elif args.command == "decompress":
#         editor.decompress()
#     else:
#         raise ValueError("No such command exists")
    

# if __name__ == "__main__":
#     main()