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
                                    "compress", "decompress", "most_active", 
                                    "most_influencer", "mutual", "suggest", 
                                    "search","draw"])
    parser.add_argument("-i", "--input", help="<file_name.xml>", type=str)
    parser.add_argument("-w", "--word", help="<word in posts>", type=str)
    parser.add_argument("-t", "--topic", help="<topic in posts>", type=str)
    parser.add_argument("-id", "--id", help="Integer id of user for suggest", type=int)
    parser.add_argument("-ids", "--ids", help="Integer ids of users for mutual", type=int, nargs='+')
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
        minified_string = editor.minify(editor.tree.root)
        editor.tree.writePrettified(args.output, minified_string)
    elif args.command == "compress":
        compressed_xml = XMLEditor.compress(args.input)
        editor.tree.writePrettified(args.output, compressed_xml)
        
    elif args.command == "decompress":
        decompressed_xml = XMLEditor.decompress(args.input)
        editor.tree.writePrettified(args.output, decompressed_xml)
        
    elif args.command == "draw":
        editor.graph.graph_draw(args.output)
        
    elif args.command == "most_active":
        user = editor.graph.most_active_user()
        if user:
            print(f"Most active user\n=======\nName: {user.name}\nID: {user.id}")
        else:
            print("None found")
            
    elif args.command == "most_influencer":
        user = editor.graph.most_influencer_user()
        if user:
            print(f"Most influencer user\n=======\nName: {user.name}\nID: {user.id}")
        else:
            print("None found")
            
    elif args.command == "mutual":
        users = editor.graph.mutual_followers(args.ids)
        print(f"Mutual Users Between Users with IDs {args.ids}\n===========")
        for i,user in enumerate(users):
            print(f"{i+1} - Name: {user.name}, ID: {user.id}")
        else:
            print("No Mutual Users")
            
    elif args.command == "suggest":
        users = editor.graph.follow_suggestions(args.id)
        print(f"Suggested Users: {[user.name for user in users]}")
    
    elif args.command == "search" and args.word:
        #TODO: print pretty post
        searched_posts_by_word = editor.graph.search_by_body(args.word)
        print([i for i in searched_posts_by_word])
        
    elif args.command == "search" and args.topic:
        #TODO: print pretty post
        searched_posts_by_topic = editor.graph.search_by_topic(args.topic)
        print(searched_posts_by_topic)
        
    else:
        raise ValueError("No such command exists")


# if __name__ == "__main__":
#     main()