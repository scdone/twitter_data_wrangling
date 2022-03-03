# twitter_data_wrangling

## About this project

>For this project, I useed three different datasets to gain insights from the WeRateDogs twitter archive. 

## Data Wrangling

>Using the Twitter Developer API and the python Tweepy library, I made requests to compile a dataset of over 2,000 tweets from their archive. In conjuction, I used two datasets from Udacity.com which contained machine learning image prediction results and archived data from the tweets. 

## Data Cleaning

>After creating a copy of the orginal datasets, I visually and programatically assessed the data using pandas in juptyer notebook. I adressed several data quality and tidiness issues, including transforming column values to appropriate data types, made casing and spacing of column names uniform, dropping or replacing NaN values, filtered out data from the API requests which was found to be uneccesary, condensed columns to abide by data tidiness rules of one column per observation, etc. A full documentation of my data cleaning effoerts can be found in reports/wrange_report.pdf in this repository. I then saved the cleaned datasets into new .csv files. 

## Data Analysis

> After wrangling and cleaning the data, I used pandas, numpy, scipy.stats, matplotlib, and seaborn to manipulate, analyze, and visualize the data. The key insights I found are detailed below:

## Key Insights

> Using dataframe query methods, I found the image predictions correctly guessed dog breeds about 71%-73% of the time. This was visualized in a bar chart showing the prediction outcomes for all three dog breed predictions of each tweet. 
> Using the pearsonr method from scipy.stats, I looked at the relationship between favorite counts and retweet counts on each tweet. The result was a correlation coefficient of 0.86 and a p-value of 0, which indicates a statistically significant strong positive correlation between the two variables. I visualized this relationship with a scatterplot using the seaborn library. 
> Using dataframe groupby and sort_values methods, I found the top five dog breeds which received the most favorite counts were Labrador Retriever, Lakeland Terrier, Chihuahua, French Bulldog, and Eskimo Dog. 

## Conclusion / What I learned

> Overall, I enjoyed this project as a fun look at the WeRateDogs twitter archive. 
> My favorite part of this project was using the Twitter API to make requests and compile my own dataset from the responses. 
> The full key insight report can be found in this repository in reports/act_report.pdf. All code for this project can be found in the wrangle_act.ipynb jupyter notebook. 
