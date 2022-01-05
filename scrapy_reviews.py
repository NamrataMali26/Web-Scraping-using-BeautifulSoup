from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.amazon.in/Apple-iPhone-11-128GB-Black/product-reviews/B07XVLW7YK/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")

soup = BeautifulSoup(r.text, 'html.parser')
Name = soup.findAll("span", {"class" : "a-profile-name"})     # find <span> element with attributes class = a-profile-name

# Extract name from span tag
Reviewer = []
for i in range(2,len(Name)):     
    Reviewer.append(Name[i].get_text())    


Product_Rating = soup.findAll("i", {"class" : "review-rating"})     # find <i> element with attributes class = review-rating
Rating = []
for i in range(2,len(Product_Rating)):     
    Rating.append(Product_Rating[i].get_text())   


Review_Title = soup.findAll("a", {"class" : "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"})     # find <a> element with attributes class = review-title-content
Review_Summary = []
for i in range(0,len(Review_Title)):
    Review_Summary.append(Review_Title[i].get_text())
Review_Summary[:] = [i.lstrip('\n').rstrip('\n') for i in Review_Summary]



Review_Description = soup.findAll("span", {"class" : "a-size-base review-text review-text-content"})     # find <span> element with attributes class = review-text-content
Description = []
for i in range(0,len(Review_Description)):
    Description.append(Review_Description[i].get_text())
Description[:] = [i.lstrip('\n').rstrip('\n') for i in Description]

# Creating dataframe & store data
Data = pd.DataFrame()
Data["Reviewer"] = Reviewer
Data["Rating"] = Rating
Data["Review Title"] = Review_Summary
Data["Review Description"] = Description
Data.to_csv('iphone_review.csv')
