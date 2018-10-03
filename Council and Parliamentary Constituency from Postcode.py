
# coding: utf-8

# In[58]:


'''
Importing Libraries for API to work and to read the JSON file
'''
import requests
import urllib
import json
from urllib.parse import urlencode
from urllib.request import urlopen


# In[59]:


def main():
    # Ask user to insert a postcode
    postcode_input = str(input("Please insert a postode:"))
    # Take the postcode, append it to the API RUL and get the response from the API
    url = "http://api.postcodes.io/postcodes/"
    url += postcode_input
    response = urlopen(url)
    # Tell Python to read the data and decode the JSON file
    response_data = response.read()
    response_data_decoded = json.loads(response_data)
    # Open the dictionary on the 'result' key
    postcode_dictionary = (response_data_decoded['result'])
    # Print the values from the Administration District and Parliamentary Constituency from 'result' dictionary
    print ("Your local council is " + postcode_dictionary['admin_district'])
    print ("Your parliamentary consituency is " + postcode_dictionary['parliamentary_constituency'])


# In[62]:


'''
This will always run main first
'''

if __name__ == "__main__":
    main()

