import os
os.environ["DJANGO_SETTINGS_MODULE"] = "djangoormsettings"  # this must be done before importing any django modules

import django
django.setup()

from src.models import Article


#TODO actually scrap data

a = Article(name='this perfect article')
a.save()

print Article.objects.all()
