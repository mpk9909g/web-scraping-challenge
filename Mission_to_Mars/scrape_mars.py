# This was saved from the jupiter notebook.   
# I did clean up some of the extra lines in this py file, 
# particularly for the section on the facts table

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
import pandas as pd
import time



def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(1)


    # In[4]:


    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)


    # In[5]:


    # HTML object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_titles = soup.find_all('div', class_='content_title')
    news_paragraphs = soup.find_all('div', class_='article_teaser_body')


    # In[6]:


    # news_titles


    # In[7]:


    # news_paragraphs


    # In[8]:


    title_texts = []
    for tit in news_titles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        title_texts.append(tit.text)
    # title_texts


    # In[9]:


    paragraph_texts = []
    for par in news_paragraphs:
        paragraph_texts.append(par.text)
    # paragraph_texts


    # In[10]:


    browser.quit()


    # In[11]:


    # now get Mars space image, yo!


    # In[12]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(1)


    # In[13]:


    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(2)


    # In[14]:


    # HTML object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(2)


    # In[15]:


    # test = soup.find('div',class_='floating_text_area')
    # test


    # In[16]:


    try:
        browser.links.find_by_partial_text('FULL IMAGE').click()
        url_root = browser.links.find_by_partial_text('FULL IMAGE')
    except:
        print("Scraping Complete")


    # In[17]:


    # HTML object
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')


    # In[18]:


    #test2 = soup.find('div',class_='footer')
    # test2 = soup.select_one('div.fancybox-inner')
    # test = soup.find('div', class_='fancybox-inner')

    test2 = soup2.find('img', class_='fancybox-image').get("src")
    test2


    # In[19]:


    browser.url


    # In[20]:


    featured_image_url = browser.url + test2
    featured_image_url


    # In[21]:


    browser.quit()


    # In[22]:


    # Now scrape Mars Facts table


    # In[23]:


    url = 'https://galaxyfacts-mars.com/'


    # In[24]:


    mars_facts_table = []
    mars_facts_table = pd.read_html(url)
    mars_facts_table

    mars_facts_table[0].rename(columns={0:"Metric",1:"Mars",2:"Earth"},inplace=True)
    mars_facts_table[1].rename(columns={0:"Metric",1:"Mars"},inplace=True)
    mars_facts_table_0 = mars_facts_table[0].iloc[1:]
    mars_facts_table[0] = mars_facts_table_0
    mars_facts_table[0].set_index("Metric", inplace = True)
    mars_facts_table[1].set_index("Metric", inplace = True)



    mars_facts_table_html = mars_facts_table[0].to_html()
    mars_facts_table_html2 = mars_facts_table_html.replace('class="dataframe"','class="table table-striped text-center"')
  


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[29]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(5)


    # In[30]:


    # HTML object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(1)


    # In[31]:


    hemispheres = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    hemisphere_image_urls = []

    for hemi in hemispheres:
        print(browser.url)
        try:
            browser.links.find_by_partial_text(hemi).click()
            url_root = browser.links.find_by_partial_text(hemi)
            time.sleep(3)
        except:
            print("Scraping Complete")
            break
        try:
            browser.links.find_by_partial_text('Sample').click()
            url_root = browser.links.find_by_partial_text('Sample')
            time.sleep(3)
            window = browser.windows[1]
            img_url = window.url
            print(img_url)
            window.close()
            browser.back()
            dict={}
            dict["title"] = hemi
            dict["img_url"] = img_url
            hemisphere_image_urls.append(dict)
        except:
            print("Scraping Complete")
            break
        


    # In[32]:


    # hemisphere_image_urls


    # In[33]:


    browser.quit()


    # In[34]:


    mars_listings = {}


    # In[35]:


    mars_listings["news_titles"] = title_texts
    mars_listings["news_paragraphs"] = paragraph_texts
    mars_listings["featured_image_url"] = featured_image_url
    mars_listings["mars_facts_table"] = mars_facts_table_html2
    mars_listings["hemisphere_image_urls"] = hemisphere_image_urls

    print("Done Scraping")
    browser.quit()
    
    return mars_listings



