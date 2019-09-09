## This function was created as an exercise at the SheCodes' Python program. 
## The function takes an url as an input and saves the image as a jpg file at ##your computer.

def sesamo(url):
    import random as r
    import urllib.request

    name = str(r.randint(1, 1001))
    
    extension = ".jpg"
    filename = name+extension

    urllib.request.urlretrieve(url, filename)


    
