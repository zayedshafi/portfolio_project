
# Sunglasshut-EDA 

I conducted an Exploratory Data Analysis (EDA) on Sunglasshut women's section by scraping the website to gather product information.

### Introduction

Over the past year and a half, I've been juggling my studies for a master's degree with my role as a retail associate at Sunglasshut. When brainstorming project ideas, I wanted something that resonated with my daily experiences, and diving into the products I sell everyday seemed like a natural fit. Particularly, I noticed a disparity in my familiarity and sales ability between women's and men's sunglasses. My project aimed to address common scenarios I encountered at work and answer questions that often crossed my mind. Here's what I focused on:

1.	Price Ranges: I wanted to understand the pricing of sunglasses across various brands. This knowledge would help me recommend products that fit within customers' budgets.
2.	New Styles: Staying up to date with the latest styles in specific brands was crucial. This way, I could inform customers about the newest trends and offerings.
3.	Discounted Items: Identifying which items were currently on sale would allow me to guide customers towards potential deals and promotions, enhancing their shopping experience.
4.	Understanding Categories: Understanding the different categories that are available like new arrivals, runway, Sunglasshut exclusive etc would again assist me in making better sales pitch.

### Methodology

•	The project followed an ETL (Extract, Transform, Load) process.

•	Selenium was used for web scraping from Sunglass Hut's women's section.

•	Pandas handled data manipulation and preparation.

•	Pymongo facilitated loading data into MongoDB Atlas due to its schema-less nature.

•	Future exploration of loading data into a relational database was discussed.

•	Power BI was used to create dashboards by connecting to MongoDB.

•	Jupyter Notebook was utilized for initial development, then code transferred to PyCharm for modular structuring.

•	Windows task scheduler use to run the scripts weekly to stay on top of the latest product details

### ETL Process

•	Website features a load button at the page's bottom, loading 18 more items with each click.

•	Load button clicked iteratively until no longer visible, ensuring comprehensive data retrieval.

•	Scraping process focuses on container holding image URLs and product information.

•	Two URLs scraped: one sorting from lowest to highest price, the other from highest to lowest.

•	Dual scraping approach ensures complete coverage of product list due to page limitations.
•	Duplicates removed during data transformation process to ensure data integrity.

•	Apart from duplicate rows a lot of string manipulation is performed to remove unwanted characters.

•	Data type conversion is performed to calculate further numerical columns.

•	After further cleaning and transformations data is returned as a dictionary to be used by the load module to host on MongoDB database.

### Demo

![](https://github.com/zayedshafi/portfolio_project/blob/master/overview.gif)
![](https://github.com/zayedshafi/portfolio_project/blob/master/allItems.gif)
![](https://github.com/zayedshafi/portfolio_project/blob/master/discountItems.gif)







### Conclusion

In conclusion, I would like to underscore the potential for further development in this project. By incorporating data from other retailers' websites, we can conduct comprehensive comparisons of product details such as pricing, discounts, and new arrivals. Additionally, there is an opportunity to enrich our dataset by retrieving additional information about the sunglasses, including lens and frame details, and delving into the specifications of each variant of a particular model. As the project evolves to handle more intricate data structures, transitioning to a relational database may become a more suitable option to manage the increased complexity effectively.
