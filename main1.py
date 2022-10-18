import imghdr
import requests
from bs4 import BeautifulSoup
import os 

#Scraping images from Airbnb Website and storing it in a folder. 

# url = 'https://www.airbnb.co.in/s/goa/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&date_picker_type=calendar&checkin=2022-11-12&checkout=2022-11-14&source=structured_search_input_header&search_type=filter_change'


def imagedown(url,folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder)) # creating a directory which is joining together the cwd and the new folder name we are giving. 
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder)) #changing directory. 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    #to find all the image tags. 
    images = soup.find_all('img') #just got elements. 

    count = 1
    for image in images: 
        if count > 12: #images 1-12 contains world maps. You can delete this line to use in general. 
            link = image['src'] #we get all the image links.  
            with open(str(count) + '.jpeg', 'wb') as f: #to save the images. |wb= write to it but know the byte as well. 
                im = requests.get(link)
                f.write(im.content) 
            print("Writing: ", str(count))
        count = count + 1
        

# imagedown( 'https://www.airbnb.co.in/s/mumbai/homes?date_picker_type=calendar&checkin=2022-11-07&checkout=2022-11-08&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=autocomplete_click','Mumbai_Airbnb')

imagedown('airbnb url','folder name')
