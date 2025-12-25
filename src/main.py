import argparse
from collections import deque
from ui.app import run_app
from xml_editor_core import XMLEditor


def verify(editor, args):
    if(args.fix):
        xml_queue = editor.verify(args.output)
        editor.tree.writeVerified(args.output, xml_queue)  # type: ignore
    else:
        xml_queue = editor.verify()


def format(editor, args):
    prettifiedOutput = editor.format()
    editor.tree.writeFromString(args.output, prettifiedOutput)


def json(editor, args):
    jsonDictionary = editor.convert(editor.tree.root)
    editor.tree.writeToJson(args.output, jsonDictionary)


def mini(editor, args):
    minified_string = editor.minify(editor.tree.root)
    editor.tree.writeFromString(args.output, minified_string)


def compress(editor, args):
    compressed_xml = XMLEditor.compress(args.input)
    editor.tree.writeFromString(args.output, compressed_xml)


def decompress(editor, args):
    decompressed_xml = XMLEditor.decompress(args.input)
    editor.tree.writeFromString(args.output, decompressed_xml)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help = "Choose a command", type=str
                        ,choices = ["verify", "format", "json", "mini",
                                    "compress", "decompress", "most_active", 
                                    "most_influencer", "mutual", "suggest", 
                                    "search","draw" , "gui"])
    parser.add_argument("-i", "--input", help="<file_name.xml>", type=str)
    parser.add_argument("-w", "--word", help="<word in posts>", type=str)
    parser.add_argument("-t", "--topic", help="<topic in posts>", type=str)
    parser.add_argument("-id", "--id", help="Integer id of user for suggest", type=int)
    parser.add_argument("-ids", "--ids", help="Integer ids of users for mutual", type=int, nargs='+')
    parser.add_argument("-f", "--fix", action="store_true")
    parser.add_argument("-o", "--output", help="<file_name.xml>", type=str)
    args = parser.parse_args()
    
    #===================================================
    #Run GUI Mode
    if args.command == "gui":
        run_app()
        return
    
    # Parses input file path from CLI
    editor : XMLEditor = XMLEditor(args.input)
    #===================================================
    #Run CLI Mode
    if args.command == "verify":
        verify(editor, args)
            
    elif args.command == "format":
        format(editor, args)
        
    elif args.command == "json":
        json(editor, args)
        
    elif args.command == "mini":
        mini(editor, args)
        
    elif args.command == "compress":
        compress(editor, args)
        
    elif args.command == "decompress":
        decompress(editor, args)
        
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
        searched_posts_by_word = editor.graph.search_by_body(args.word)
        print([i for i in searched_posts_by_word])
        
    elif args.command == "search" and args.topic:
        searched_posts_by_topic = editor.graph.search_by_topic(args.topic)
        print(searched_posts_by_topic)
        
    else:
        raise ValueError("No such command exists")


if __name__ == "__main__":
    main()