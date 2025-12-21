from xml_tree import XNode


class User:
    def __init__(self, id:int = 0):
        self.id = id
        self.name = ""
        self.followers = []
        self.degree = 0
        self.posts = []

class Post:
    def __init__(self, id = 0):
        self.body = ""
        self.topics = []
        self.user_id = id

class GraphMaker:
    def __init__(self, root : XNode) -> None:
        self.adjMatrix = [[0] * 1000 for _ in range(1000)]
        self.users = [User(0) for i in range(1000)]
        self.graph = [[] for _ in range (1000)]
        self.posts=[]
        self.root = root
        self.generate_graph()
        
    def generate_graph(self):
        if self.root:
            children = self.root.children
            for child in children:
                if child.tag=="user":
                    user_id = findUserId(child)
                    if self.users[user_id] is None:
                        self.users[user_id] = User(user_id)

                    self.users[user_id].id = user_id
                    user_name = findUserName(child)
                    self.users[user_id].name = user_name

                    user_followers = get_user_followers(child)
                    for follower in user_followers:
                        if self.users[follower] is None:
                            self.users[follower] = User(follower)

                        self.users[follower].id = follower
                        self.users[user_id].followers.append(self.users[follower])
                        self.users[user_id].degree+=1
                        self.users[follower].degree+=1
                        self.adjMatrix[user_id][follower] = 1

                    user_posts = get_user_posts(child)
                    for post in user_posts:
                        self.posts.append(post)
                    self.users[user_id].posts = user_posts


    def most_influencer_user(self):
        max_followers = -1
        most_influencer = None
        for user in self.users:
            if user.id!=0:
                if len(user.followers) > max_followers:
                    most_influencer = user
                    max_followers = len(user.followers)
        return most_influencer

    def most_active_user(self):
        max_active = -1
        most_active = None
        for user in self.users:
            if user.id != 0:
                if user.degree > max_active:
                    most_active = user
                    max_active = user.degree

        return most_active

    def mutual_followers(self, users: list[int]):
        mutual=[]
        for i in range(len(self.adjMatrix)):
            flag = True
            for user in users:
                if self.adjMatrix[user][i]==0:
                    flag = False
                    break
            if flag:
                mutual.append(self.users[i])

        return mutual

    def follow_suggestions(self, user_id: int):
        suggestions = []
        for follower in self.users[user_id].followers:
            for suggestion in self.users[follower.id].followers:
                if (suggestion.id != user_id) and (self.adjMatrix[user_id][suggestion.id] == 0):
                    suggestions.append(suggestion)

        return suggestions

    def search_by_body(self, word:str):
        searched_posts = []
        for post in self.posts:
            if str(post.body).find(word)!=-1:
                searched_posts.append(post)

        return searched_posts

    def search_by_topic(self,word:str):
        searched_posts = []
        for post in self.posts:
            for topic in post.topics:
                if str(topic).find(word) != -1:
                    searched_posts.append(post)
                    break

        return searched_posts        
        
# HELPER FUNCTIONS

def findUserId(user:XNode):
    for child in user.children:
        if child.tag == "id":
            return int(child.text)

    return 0

def findUserName(user:XNode):
    for child in user.children:
        if child.tag == "name":
            return child.text

    return ""

def get_user_followers(user:XNode):
    followers = []
    for child in user.children:
        if child.tag == "followers":
            for follower in child.children:
                if follower.tag=="follower":
                    followers.append(findUserId(follower))

    return followers

def get_user_posts(user:XNode):
    posts = []
    user_id = findUserId(user)
    for child in user.children:
        if child.tag == "posts":
            for post in child.children:
                if post.tag=="post":
                    posts.append(post)
    posts_details = []
    for post in posts:
        p = Post()
        p.user_id = user_id
        for content in post.children:
            if content.tag == "body":
                p.body = content.text
            if content.tag == "topics":
                for topic in content.children:
                    p.topics.append(topic.text)
        posts_details.append(p)

    return posts_details

