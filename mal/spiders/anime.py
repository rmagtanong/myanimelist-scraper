import scrapy
import mal.constants as constants
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AnimeSpider(CrawlSpider):

    name = 'anime'
    allowed_domains = ['myanimelist.net']
    start_urls = [constants.START_URL]

    user_agent = constants.USER_AGENT

    def start_requests(self):
        ''''
        url structure:
        https://myanimelist.net/topanime.php?limit=0
        https://myanimelist.net/topanime.php?limit=50
        https://myanimelist.net/topanime.php?limit=100
        '''
        limit_list = list(range(0, 10001, 50))
        for index in limit_list:
            yield scrapy.Request(url=f'{constants.MYANIMELIST_URL}?limit={index}',
                                 headers={'User-Agent': self.user_agent})

    rules = (
        # get all anime in page
        Rule(LinkExtractor(
            restrict_xpaths=constants.ANIME_URL),
            callback='parse',
            follow=True,
            process_request='set_user_agent'),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse(self, response):
        yield {
            'anime_id': self.get_anime_id(response.url),
            'name': response.xpath(constants.ANIME_NAME).get(),
            'rating': self.to_float(response.xpath(constants.ANIME_RATING).get()),
            'genres': response.xpath(constants.ANIME_GENRES).getall(),
            'users_watched': self.to_int(response.xpath(constants.USERS_WATCHED).get()),
            'users_rated': self.to_int(response.xpath(constants.USERS_RATED).get()),
            'url': response.url,
        }

    @staticmethod
    def get_anime_id(url):
        split_url = url.split('/')
        return split_url[4]

    @staticmethod
    def to_int(num):
        num = num.replace(',', '')
        return int(num)

    @staticmethod
    def to_float(num):
        return float(num)

