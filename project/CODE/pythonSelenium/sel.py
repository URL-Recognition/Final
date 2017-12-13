import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import pyautogui


def main():
    '''

        For issues running with error "'chromedriver' executable needs to be in PATH."

        run the commands:
                            export PATH=$PATH:~/Desktop/pythonSelenium/
                            export PATH=$PATH:~/Desktop/pythonSelenium/chromedriver
                            python3 sel.py



    '''



    #start chrome fullscreen. PyautoGui will only take a screenshot of the entire screen.
    chromeOptions = Options()
    chromeOptions.add_argument('--start-fullscreen')
    browser = webdriver.Chrome(chrome_options=chromeOptions)

    file = open('links.txt', 'r')
    urls_list = file.read()
    urls = set(urls_list.split('\n'))
    # wait because chrome will open with a banner at the top.
    # the script will wait for input so you can manually close the banner.
    # after running the script, close the banner and then switch back to the script
    # and enter a newline. Make sure to switch back to the banner.
    x = input()
    count = 0
    for url in list(urls):
        try:
            browser.get(url)
        except:
            continue
        time.sleep(1)
        im = pyautogui.screenshot('screenshots/url_screenshot' + str(count) + '.png')
        count = count + 1
        #count = takeScreenshot(browser, count)                                                                                                                           
        #count = crawl(browser, count)                                                                                                                                    

    browser.quit()
    file.close()


    
    ''' partial code for firefox web-crawler.

    fbrowser = webdriver.Firefox()
    fbrowser.get('https://google.com')
    
    count = 0;
    file = open('links.txt', 'r')
    urls_list = file.read()
    urls = set(urls_list.split('\n'))
    x = input()
    count += 1

    for url in list(urls):
        try:
            fbrowser.get(url)
        except:
            continue
        time.sleep(1)
        im = pyautogui.screenshot('url_screenshotf' + str(count) + '.png')
        count = count + 1
        count = takeScreenshot(fbrowser, count)

    fbrowser.quit()
    file.close()
    '''

def takeScreenshot(driver, count, new_link):
    '''
    :param driver: Driver for a webrowser
    :param count: The count of the screenshot taken. Used for naming saved file.
    :param new_link: Link to navigate
    :return: An updated count.

    This function will navigate to a new link that is passed in, wait for the page to load,
    and then take a new screenshot. If the screenshot was successful, it will save the new
    screenshot and increment the counter.
    '''

    try:
        driver.get(new_link)
        time.sleep(2)
        im = pyautogui.screenshot('url_screenshot' + str(count) + '.png')
        count = count + 1
    except Exception as e:
        return count

    return count

def crawl(driver, count):
    '''
    :param driver: Driver for a webrowser
    :param count: The count of the screenshot taken. Used for naming saved file.
    :return: An updated count.

    This function will collect the first 15 unique links for the current page.
    It will output these links to the console.
    '''
    anchors = driver.find_elements_by_tag_name('a')[:15]
    hrefs = []
    for i in range(len(anchors)):
        link = anchors[i].get_attribute('href')
        if link != None and 'http' in link:
            print(link)
            hrefs.append(link)


    ''' This code will take a screenshot of all the collected links
        It is commented out because during the actual collection of screenshots,
        we just saved all of the harvested links to a text file and did a normal webcrawl.
    iter = 0 # stop after 10 interations
    for link in hrefs:

        print(link)
        count = takeScreenshot(driver, count, link)
        iter += 1
        if iter == 10:
            return count
    '''
    return count

main()
