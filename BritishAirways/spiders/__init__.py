import scrapy

#create a class review to crawl the review website
class review(scrapy.Spider):
    name = "review"

    #provide the start url

    start_urls = ["https://www.airlinequality.com/airline-reviews/british-airways/?sortby=post_date%3ADesc&pagesize=50"]

    #function to parse the reviews

    def parse(self, response):
        #storing the reviews in a variable
        reviews = response.xpath("//article[@itemprop='review']") 

        #parsing the individual reviews
        for review in reviews:
            review_data =  {
                "name": review.css("span[itemprop='name']::text").get(),
                "rating": review.css("span[itemprop='ratingValue']::text").get(),
                "date": review.css("time[itemprop='datePublished']").attrib['datetime'],
                "text": review.css("div.text_content::text")[-1].get().replace(" |  ","").replace(" | ","")
            }
            #extracting data from the table element
            rows = review.css("tr")
            columns = []
            for row in rows:
                columns.append(row.css("td"))
            for column in columns:
                if column[1].css("::text").getall() == ['1', '2', '3', '4', '5']:
                    review_data[column[0].css("::text").get()] = len(column[1].css("span.fill"))    #extracting the star ratings in the review
                else:
                    review_data[column[0].css("::text").get()] = column[1].css("::text").get()

            yield review_data

        # finding the element that consists the link to the next page

        next_page = response.css("article.querylist-pagination.position-").css('li')[-1].css("a").attrib['href']
        #crawling and parsing the next page
        
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)
