
# coding: utf-8

# In[7]:


from splinter import Browser
from bs4 import BeautifulSoup
import requests


# In[10]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[12]:


html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[13]:


slide_elem.find("div", class_='content_title')


# In[6]:


slide_elem.find("div", class_='content_title')


# In[14]:


news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[15]:


news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[16]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[17]:


full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[18]:


browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


# In[19]:


html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[20]:


img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[21]:


img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[22]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[23]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[24]:


# First, find a tweet with the data-name `Mars Weather`
mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})


# In[25]:


# Next, search within the tweet for the p tag containing the tweet text
mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# In[ ]:


jupyter nbconvert --to FORMAT notebook.ipynb

