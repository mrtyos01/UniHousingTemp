import scrapy


class KamernetSpider(Scrapy.Spider):
    name = 'Kamernet_Rooms'

    init_url = ['https://kamernet.nl/huren/kamers-nederland']

    custom_settings = { 'FEED_URI': "Kamernet_%(time)s.json",
                        'FEED_FORMAT': 'json'}


    def parse(self, response):

        # Extracting data using css selectors
        
        room_link = response.css("div.tile-img a::attr(href)").extract()

        city_name = response.css("div.tile-city::text").extract()

        rent = response.css("div.tile-rent::text").extract()

        room_type = response.css("div.tile-room-type::text").extract()

        surface = response.css("div.tile-surface::text").extract()

        furnished = response.css("div.tile-furnished::text").extract()        

        fa_calendar = response.css("div.left::text").extract()

        row_data = zip(city_name,room_link,rent,room_type,surface,furnished,fa_calendar)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                'city_name' : item[0],
                'room_link' : item[1],
                'rent' : item[2],
                'room_type' : item[3],
                'surface' : item[4],
                'furnished' : item[5],
                'fa_calendar' : item[6]
            }

            # yield or give the scraped info to Scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = '.pagination + a::attr(href)'

            # you first extracted the link of the next page using
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

            # if the variable next_page gets a link and is not empty, it will enter the if body.
            if next_page:
                yield scrapy.Request(
                    # The parse() method will use this method to build a new url and
                    # provide a new request, which will be sent later to the callback.
                    
                    response.urljoin(next_page),
                    callback = self.parse
                )
            
            # After receiving the new URL, it will scrape that link executing the for body and again look for the next page.
            # This will continue until it doesn't get a next page link.