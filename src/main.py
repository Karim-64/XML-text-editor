import argparse
from xml_editor_core import XMLEditor

#==========
#TODO:
# rename writePrettified to writeFromString
#==========

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help = "Choose a command", type=str
                        ,choices = ["verify", "format", "json", "mini",
                                    "compress", "decompress"])
    parser.add_argument("-i", "--input", help="<file_name.xml>", type=str)
    parser.add_argument("-f", "--fix", action="store_true")
    parser.add_argument("-o", "--output", help="<file_name.xml>", type=str)
    args = parser.parse_args()
    
    #===================================================
    # Parses input file path from CLI
    editor : XMLEditor = XMLEditor(args.input)
    #===================================================
    
    if args.command == "verify":
        editor.verify()
    elif args.command == "format":
        prettifiedOutput = editor.format()
        editor.tree.writePrettified(args.output, prettifiedOutput)
    elif args.command == "json":
        jsonDictionary = editor.convert(editor.tree.root)
        editor.tree.writeToJson(args.output,jsonDictionary)
    elif args.command == "mini":
        editor.minify()
        
    elif args.command == "compress":
        compressed_xml = XMLEditor.compress(args.input)
        editor.tree.writePrettified(args.output, compressed_xml)
        
    elif args.command == "decompress":
        decompressed_xml = XMLEditor.decompress(args.input)
        editor.tree.writePrettified(args.output, decompressed_xml)
    else:
        raise ValueError("No such command exists")


# if __name__ == "__main__":
#     main()