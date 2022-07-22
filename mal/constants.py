# setup
MYANIMELIST_URL = 'https://myanimelist.net/topanime.php'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'

# xpaths
START_URL = 'https://myanimelist.net/topanime.php'
ANIME_URL = '//h3[@class="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3"]/a'
NEXT_PAGE = '//a[@class="link-blue-box next"][1]'

ANIME_NAME = '//h1/strong/text()'
ANIME_RATING = '//div[@class="fl-l score"]/div/text()'
ANIME_GENRES = '//span[@itemprop="genre"]/text()'
USERS_WATCHED = '//span[@class="numbers members"]/strong/text()'
USERS_RATED = '//div[@itemprop="aggregateRating"]/span[@itemprop="ratingCount"]/text()'
