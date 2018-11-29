
import requests, bs4, webbrowser,sys 

def price (website, css):

    res = requests.get(website)
    #check download was successful
    res.raise_for_status() # if there is an issue with the response it will raise an exception


    #parse the html in other to help us get the element of the value we are lookin 4
    #parsing changes the html format so that it is easier for us to locate the element of the particular info
    #we are looking for

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #next we use the css selector of this element to find it. 
    #they help u specify a particular par of the HTML that u want to look at

    elems = soup.select(css)

    return (elems[0].text) 


website1 = 'https://www.zappos.com/p/ugg-bailey-bow-tall-ii-black/product/8945647/color/3'
css = '#productRecap > div._7Ri0r > aside > div._3FeqD > div > div > span'
ans = price(website1, css)
print(ans) # 249.95


website2 = 'https://www.zappos.com/p/ugg-sundance-waterproof-black/product/8911372/color/3?zlfid=191&ref=pd_detail_ext_search_v_2' 
css = '#productRecap > div._7Ri0r > aside > div._3FeqD > div > div > span'
ans1 = price(website2,css)
print(ans1)  # 249.95

    

print ('The price of the UGG Bailey Bow Tall II was 249.95, now it is ' +ans)
getting1 = input('would you be interested in getting it?')

if getting1.lower()  == 'yes':

    webbrowser.open(website1)

    sys.exit()

    
print ('The price of the UGG Sundance Waterproof was 249.95, now it is ' +ans1)

getting2 = input('would you be interested in getting it?')

if getting2.lower() == 'yes':

    webbrowser.open(website2)
           

    
