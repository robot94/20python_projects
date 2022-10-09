#Welcome to the URL checker

import urllib.request as urllib


def main(url):
    
    print("Cheking connectivity...")
    
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code is:", response.getcode())
    
    
print("This is a site connectivity checker")

input_url = input("Please entre the URL that you want to test: ")

main(input_url)


    