import scrapy
from project_book_scraper.items import BookScraperItem
from scrapy.loader import ItemLoader


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            book_url = book.css("a::attr(href)").get()

            yield response.follow(book_url, callback=self.parse_book)


        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def parse_book(self, response):

        loader = ItemLoader(item=BookScraperItem(), response=response)

        loader.add_css('title', 'h1::text')
        loader.add_css('price', 'p.price_color::text')
        loader.add_css('stock', 'p.instock.availability')
        loader.add_css('rating', 'p.star-rating::attr(class)')
        loader.add_css('category', 'ul.breadcrumb li:nth-child(3) a::text')
        loader.add_css('description', 'div#product_description + p::text')

        yield loader.load_item()