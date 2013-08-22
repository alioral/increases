from mongoengine import *

# Create your models here.

class Page(Document):
	path = StringField()
	visitors = IntField()
	change = IntField()
	owner = StringField()