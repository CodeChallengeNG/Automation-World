

from selenium import webdriver # using the selenium module, and a chrome driver, i can automatically start a google chrome page 

import time 

browser = webdriver.Chrome(r'C:/Users/aadetola/Desktop/chromedriver.exe') # path of the driver 

browser.get('https://www.youtube.com/watch?v=QIC26FzCsPM&index=10&list=RD5KFpMIeW9YA')  #my fav song on youtube :) 



for i in range(10): # yes i can listen to a song 10 times straight :) 

    time.sleep(175)	#the song starts playing here and so i wait 3 mins roughly before i hit replay

    pause = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')

    pause.click() #pausing the song, not necessary to but i felt like. i am using the css selector of the pause button and the click method

    rewind = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-prev-button.ytp-button')

    rewind.click() # Now i am clicking on the rewind/back button of the video music player  

    play = browser.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')

    play.click() # Now i am clicking on the play button using the css selector. 






		
		
	
