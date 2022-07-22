# myanimelist-scraper

___

This scrapes the top 10,000 anime on [MyAnimeList](https://myanimelist.net/topanime.php). The spider will visit every
anime's page and scrape the following information:

- **anime_id:** unique id set by MyAnimeList
- **name:** anime name
- **rating:** anime rating
- **genres:** anime genres
- **users_watched:** number of users who have watched the anime
- **users_rated:** number of users who rated the anime
- **url:** anime's MyAnimeList url

The results were stored in **anime.csv**. For those unfamiliar with Scrapy, most of the logic can be found in **mal/spiders/anime.py**

Notes:
- The **genres** field is the combination of an anime's Genres, Themes, and Demographic. Ideally these would have their
own fields but their XPaths are exactly the same. Indexing could not be used since it was inconsistent per page.
- The number of **episodes** could not be scraped due to the XPath being inconsistent per page.

