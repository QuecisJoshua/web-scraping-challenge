#!/usr/bin/env python
# coding: utf-8

# In[32]:
import pandas as pd
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup


import time
import requests


# In[33]:

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    return Browser("chrome", **executable_path, headless=False)


# In[34]:

def scrape_info():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html


# In[35]:


    soup = BeautifulSoup(html, 'html.parser')
    article = soup.select_one("ul.item_list li.slide")
    title = article.find("div", class_ = "content_title").text
    paragraph = article.find("div", class_ = "article_teaser_body").text
    title = article.find("div", class_ = "content_title").text

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html_image = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url = 'https://www.jpl.nasa.gov'
    mage_url = main_url + image_url
    
    mars_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(mars_url)
    soups = BeautifulSoup(response.text, 'lxml')
 
    tweets = []
    for tw in soups.find_all("li", {"data-item-type": "tweet"}): 
        tweetsa = []
        let = tw.find("p", class_="tweet-text")
        if let is not None:
            tweetsa.append(let.get_text())
            for i in tweetsa: 
                twee = []
                twee.append(i)
                if any("sol" in s for s in twee):
                    tweetsa.append(i)

                mars_weather = str(tweetsa[0])
                mars_weather

    mars_weather = str(tweetsa[0])
# In[46]:


    facts_url = 'https://space-facts.com/mars/'
    facts_tables = pd.read_html(facts_url)
    mars_df=facts_tables[0]
    mars_df.columns=["descript","value"]
    mars_df.set_index("descript",inplace=True)
    mars_html_table=mars_df.to_html()
    mars_html_table.replace('\n','')


# In[49]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres1=soup.find("div",class_='collapsible results')
    hemisphere1=hemispheres1.find_all('a')
    main_url="https://astrogeology.usgs.gov/"
    hemisphere_image_urls=[]
    for hemispheres1 in hemisphere1:
        if hemispheres1.h3:
            title=hemispheres1.h3.text
            link=hemispheres1["href"]
            forward_url=main_url+link
            browser.visit(forward_url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            hemi2=soup.find("div",class_= "downloads")
            image=hemi2.ul.a["href"]
            hemi_dict={}
            hemi_dict["title"]=title
            hemi_dict["img_url"]=image
            hemisphere_image_urls.append(hemi_dict)
            browser.back()

    hemisphere_image_urls


    browser.quit()
    return mars_py_dict

