import factory
from . import models

class PostFactory(factory.Factory):
    class Meta:
        model = models.Model

    title = 'Test Title'
    text = 'Hello World!'
    admin = False
