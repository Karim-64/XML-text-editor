import argparse
from xml_editor_core import XMLEditor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help = "Choose a command", type=str
                        ,choices = ["verify", "format", "json", "mini",
                                    "compress", "decompress", "most_active", 
                                    "most_influencer", "mutual", "suggest", 
                                    "search"])
    parser.add_argument("-i", "--input", help="<file_name.xml>", type=str)
    parser.add_argument("-w", "--word", help="<word in posts>", type=str)
    parser.add_argument("-t", "--topic", help="<topic in posts>", type=str)
    # parser.add_argument("-ids", "--ids", help="<file_name.xml>", type=str)
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
        editor.compress()
    elif args.command == "decompress":
        editor.decompress()
    elif args.command == "most_active":
        user = editor.graph.most_active_user()
        if user:
            print(user.name)
            print(user.id)
    elif args.command == "most_influencer":
        user = editor.graph.most_influencer_user()
        if user:
            print(user.id)
            print(user.name)
    elif args.command == "mutual":
        user1 = editor.graph.most_influencer_user()
        user2 = editor.graph.most_active_user()
        if user1 and user2:
            user = editor.graph.mutual_followers([1,2])
            if user:
                print(user[0].id)
                print(user[0].name)
            else:
                print("mfeesh")
    elif args.command == "suggest":
        #TODO: parse id from cli
        x = editor.graph.follow_suggestions(1)
        print(x)
    elif args.command == "search":
        #TODO: print pretty post
        x = editor.graph.search_by_body(args.word)
        print([i.id for i in x][0])
        print([i.body for i in x][0])
        print([i.body for i in x][0])
    elif args.command == "search":
        #TODO: print pretty post
        x = editor.graph.search_by_body(args.word)
        print([i.id for i in x][0])
        print([i.body for i in x][0])
        print([i.body for i in x][0])
    else:
        raise ValueError("No such command exists")
    

# if __name__ == "__main__":
#     main()