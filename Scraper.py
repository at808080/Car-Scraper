from selenium import webdriver
from selenium.webdriver.common.keys import Keys as Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
DRIVERPATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(DRIVERPATH)

driver.get("https://www.gumtree.com.au/")

searchfield = driver.find_element_by_id("search-query")
searchfield.send_keys("4runner")
searchfield.send_keys(Keys.RETURN)


try: 
    main = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-page__user-ad-collection")))
    print(main.text)

    try: 
        #listings = main.find_elements_by_class_name("user-ad-row-new-design user-ad-row-new-design--cars-category link link--base-color-inherit link--hover-color-none link--no-underline")
        listings = main.find_elements_by_xpath("div/div/a")
        #listings = main.find_elements_by_xpath("div/div")
        print("LISTINGS[4]: ")
        print(listings[4].text)
        print(listings)
        print("Listings type: " + str(type(listings)))
        print("Listings length = " + str(len(listings)))
    except:
        driver.quit()
except:
    driver.quit()


'''
listingspage = driver.find_elements_by_class_name("user-ad-collection-new-design")
#print(listingspage.text)
#print(driver.page_source)

'''
#driver.quit()