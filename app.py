from database import Database
from menu import Menu
from models.blog import Blog

Database.initialize()

menu = Menu()

menu.run_menu()