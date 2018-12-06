

from selenium import webdriver

import time 

browser = webdriver.Chrome(r'C:/Users/aadetola/Desktop/chromedriver.exe')

browser.get('https://www.youtube.com/watch?v=QIC26FzCsPM&index=10&list=RD5KFpMIeW9YA')



for i in range(1):

    time.sleep(170)	

    pause = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')

    #goback = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-prev-button.ytp-button')

    pause.click()

    rewind = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-prev-button.ytp-button')

    rewind.click()


    play = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')

    play.click()



for i in range(10): 

	next_song = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button')

	next_song.click()
	
	time.sleep(15)

	print('skip?')
	
	ans = input()
	
	if ans.lower() == 'yes': 
	
		continue
		
	else: 

		time.sleep(170)
		
		
		
	