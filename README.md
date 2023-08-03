# Scraping Reviews and ratings using scrapy
This is a project that scrapes reviews from the website skytrax and ratings in different categories using scrapy. It scrapes every information in each block of the review from information like the aircraft the passenger flew, date, ratings for each service they recieved, etc.

The spider used to scrape the reviews is in the file BritishAirways/spiders/__ init__.py file.


<img width="842" alt="image" src="https://github.com/hakkam10/scraping-reviews-and-ratings-using-scrapy/assets/65278539/2a6e272a-a98c-4de4-b0f8-a5dcd82986ce">


This is what a review block in the site looks like. Every information from this block is scraped into a seperate column and stored in a json file.

The json file is called output.json
