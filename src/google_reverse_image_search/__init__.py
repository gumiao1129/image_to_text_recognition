import os
import base64
import urllib.request
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import json
import re

class ReverseImageSearch:
    """
            This is google reverse search tool which allow users to convert the image to text.
            The images are passed by URL, which support mutiplie images search
    """

    def __init__(self):
        self.__googleImageAPI  = 'http://images.google.com/searchbyimage?image_url='
        self.__addHeader = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
        self.imageURL = ''

    def setImageURL(self, imageURL):
        self.imageURL = imageURL

    def imageToText(self):
        if(self.imageURL != ''):
            googlePath = self.__googleImageAPI + self.imageURL
            request  = urllib.request.urlopen(googlePath)
            response = request.read()
            soup = BeautifulSoup(response, 'html.parser')
            soup.prettify()
            tag = soup.find('input',attrs={"class":"gLFyf gsfi", "maxlength":"2048", "type": "text"})
            return tag.get('value')
        else:
           raise ValueError("An error occured! Please set imageURL") 