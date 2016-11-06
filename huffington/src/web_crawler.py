from src.models import ArticleOrComment, Author


class WebCrawler(object):
    def __init__(self, url, existing_crawlers_urls):
        """
        creates a new web crawler object with given url and a set of parent web crawlers urls in order to prevent loops.
        :param url: String
        :param existing_crawlers_urls: set(String)
        :return:
        """
        self.url = url
        self.existing_crawlers_urls = existing_crawlers_urls

    def crawl(self):
        """
        crawls the given url, and returns a list of all possible objects to be created.
        """

        objects = []

        # First check the given url

        if is_article(self.url):
            pass
            # TODO: get the author, date, and comments from the given url and add it to 'objects' list

        # then crawl the rest of the urls

        url_list = find_urls(self.url)
        full_url_list = url_list + self.existing_crawlers_urls
        crawlers = []

        for url in url_list:
            if url not in self.existing_crawlers_urls:  # anti loop
                crawlers.append(WebCrawler(url, full_url_list))

        for crawler in crawlers:
            objects.extend(crawler.crawl())

        return objects


def find_urls(input_string):
    """
    parses the input string and returns a list of all url's which can be found in it.
    it is assumed that this input_string is a raw html file.
    :param input_string: String
    :return: [String]
    """
    # TODO
    return []


def is_article(url):
    """
    checks if there is an article under given url
    :param url:
    :return:
    """

    # possible idea: articles contain word 'entry' in their url's

    return False  # TODO

