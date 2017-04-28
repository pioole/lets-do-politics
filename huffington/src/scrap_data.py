import os
os.environ["DJANGO_SETTINGS_MODULE"] = "djangoormsettings"  # this must be done before importing any django modules

import django
django.setup()

from src.models import Comment
from src.web_crawler import WebCrawler


crawler = WebCrawler('http://www.huffingtonpost.com/')

object_list = crawler.crawl()

for object_ in object_list:
    object_.save()

print ArticleOrComment.objects.all()
