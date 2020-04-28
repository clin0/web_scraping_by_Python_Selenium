import csv
from selenium import webdriver

# open a webpage in Chrome
driver = webdriver.Chrome('driver\chromedriver.exe')

'''
max_page_num = 5
max_page_dig = 3
for i in range(1, max_page_num+1):
    page_num = str(i).zfill(max_page_dig)
    url = 'http://econpy.pythonanywhere.com/ex/{}.html'.format(page_num)
'''

max_page_num = 5
for i in range(1, max_page_num+1):
    url = 'http://econpy.pythonanywhere.com/ex/{:03d}.html'.format(i)

    # open a webpage in Chrome
    driver.get(url)

    # extract lists of 'buyer' and 'pries' based on xpath
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    num_page_items = len(buyers)
    with open('result.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + ',' + prices[i].text + "\n")

driver.close()


'''
## For the first page only
# open a webpage in Chrome
driver = webdriver.Chrome('driver\chromedriver.exe')

driver.get('http://econpy.pythonanywhere.com/ex/001.html')

# extract lists of 'buyer' and 'pries' based on xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
#print(buyers)
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
#print(prices)


# print out all of he buyers and prices on the current page
num_page_items = len(buyers)

for i in range(num_page_items):
    print(buyers[i].text + ": "+ prices[i].text)

# close the browser
driver.close()
'''