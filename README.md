# Sales & Customer Analytics

## Project Overview

This project analyzes Superstore sales data to identify sales trends, customer behavior, product performance, regional performance, and shipping patterns.

The project follows an end-to-end data analytics workflow using Excel, MySQL, Python, and Power BI.

## Objective

The main objectives of this project are to:

- Analyze overall sales performance
- Identify yearly and monthly sales trends
- Compare sales across product categories and sub-categories
- Analyze regional and city-level performance
- Understand customer segment behavior
- Identify top customers and products
- Analyze order and customer metrics
- Evaluate shipping performance
- Present business insights through an interactive Power BI dashboard

## Tools & Technologies

- Excel
- MySQL
- Python
- Pandas
- Matplotlib
- Power BI

## Dataset

The dataset contains 9,800 sales records covering the period from 2015 to 2018.

The dataset includes information related to:

- Orders
- Customers
- Products
- Categories
- Sub-Categories
- Regions
- Cities
- Sales
- Shipping dates
- Shipping modes

The raw dataset is not included in this repository.

## Project Workflow

Raw Data  
↓  
Excel Data Cleaning  
↓  
MySQL Data Import & SQL Analysis  
↓  
Python Exploratory Data Analysis  
↓  
Power BI Dashboard  
↓  
Business Insights

## Data Cleaning – Excel

The data was prepared and validated using Excel.

The following fields were added:

- Order Year
- Order Month
- Shipping Days

Data quality checks included:

- Duplicate record checking
- Missing value checking
- Date validation
- Sales data validation
- Category and segment validation

## SQL Analysis – MySQL

MySQL was used to perform business-oriented analysis, including:

- Total sales
- Sales by year
- Sales by category
- Sales by region
- Top customers
- Top products
- Total orders
- Average Order Value
- Sales by customer segment
- Sales by sub-category
- Monthly sales trends
- Average shipping time
- Top cities by sales
- Region and category analysis
- Customer order frequency
- Shipping performance
- Above-average customer analysis
- Customer sales ranking
- Year-over-year sales changes

## Python Analysis

Python was used for exploratory data analysis using:

- Pandas
- Matplotlib

The analysis included:

- Dataset structure and data types
- Missing value analysis
- Duplicate checking
- Descriptive statistics
- Sales by category
- Sales by region
- Sales trends by year
- Sales by sub-category
- Top customers
- Top cities
- Customer analysis
- Shipping analysis

## Power BI Dashboard

An interactive Power BI dashboard was created to present the key findings.

### Dashboard Components

- Total Sales
- Total Orders
- Total Customers
- Sales by Category
- Sales by Region
- Sales Trend by Year
- Sales by Customer Segment
- Top 10 Cities by Sales
- Sales by Sub-Category
- Sales by Shipping Category

## Key Business Insights

### Sales Performance

Sales increased significantly after 2016, with 2018 recording the highest annual sales.

| Year | Sales |
|---|---:|
| 2015 | 479,856 |
| 2016 | 459,436 |
| 2017 | 600,193 |
| 2018 | 722,052 |

### Category Performance

Technology generated the highest sales among the three main categories.

| Category | Sales |
|---|---:|
| Technology | 827,456 |
| Furniture | 728,659 |
| Office Supplies | 705,422 |

### Regional Performance

The West region generated the highest sales in the SQL analysis.

| Region | Sales |
|---|---:|
| West | 702,191 |
| East | 669,519 |
| Central | 492,647 |
| South | 389,151 |

### Customer Segment

The Consumer segment generated the highest overall sales.

- Consumer: 1,148,061
- Corporate: 688,494
- Home Office: 424,982

Home Office had the highest Average Order Value among the three segments.

### Product Performance

Phones was the highest-selling sub-category, followed closely by Chairs.

### Shipping Performance

Standard shipping was the most commonly used shipping category.

- Standard: 2,946 orders
- Fast: 1,089 orders
- Slow: 887 orders

The average shipping time was approximately 4 days.

## Project Structure

```text
Sales-Customer-Analytics/
│
├── sales_analysis.py
├── Sales_Customer_Analytics_Dashboard.pbix
└── README.md
```
## Conclusion

This project demonstrates an end-to-end data analytics workflow, from data cleaning and SQL analysis to Python exploration and Power BI visualization.

The analysis helped identify important patterns in sales performance, customers, products, regions, and shipping, and converted the findings into business-oriented insights.
