# Scraping Reviews and ratings using scrapy
This is a project that scrapes reviews from the website skytrax and ratings in different categories using scrapy. It scrapes every information in each block of the review from information like the aircraft the passenger flew, date, ratings for each service they recieved, etc.

The spider used to scrape the reviews is in the file BritishAirways/spiders/__ init__.py file.

This is what a review block in the site looks like. Every information from this block is scraped into a seperate column and stored in a json file.

<img width="839" alt="image" src="https://github.com/hakkam10/scraping-reviews-and-ratings-using-scrapy/assets/65278539/7200514d-ce73-46a1-acc5-d17dafa9ab45">



The json file is called output.json

This is how the extracted file looks like.

<img width="1165" alt="image" src="https://github.com/hakkam10/scraping-reviews-and-ratings-using-scrapy/assets/65278539/13949c7b-d20d-476d-9015-c956625b2435">




