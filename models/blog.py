import uuid
import datetime

from database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.description = description
        self.title = title
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('enter post title: ')
        content = input('enter post content: ')
        #date = input('enter post date (in format DDMMYYYY): ')
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.utcnow(),
                    id=None)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())


    def json(self):
        return {
            'id': self.id,
            'author': self.author,
            'description': self.description,
            'title': self.title,
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection = 'blogs',
                                      query = {'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])