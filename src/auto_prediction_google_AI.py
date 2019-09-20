from imageai.Prediction import ImagePrediction
import os
import base64
import urllib.request
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import json
import re


execution_path = os.getcwd()

prediction = ImagePrediction()
# ResNet50
# prediction.setModelTypeAsResNet()
# prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
# prediction.loadModel()

# DenseNet121
# prediction.setModelTypeAsDenseNet()
# prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
# prediction.loadModel()

# InceptionV3 
# prediction.setModelTypeAsInceptionV3()
# prediction.setModelPath(os.path.join(execution_path, "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
# prediction.loadModel()

# SqueezeNet 
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

#predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "../1.jpg"), result_count=10)
#url = 'https://bestoshare.com/server/php/files/19_2_general/1809091541272c2d72c6cdcd87f4d9ef.jpg'
# response = requests.get(url)
# uri = ("data:" + 
#        response.headers['Content-Type'] + ";" +
#        "base64," + base64.b64encode(response.content).decode("utf-8"))
#print(uri)


execution_path = os.getcwd()
opener = urllib.request.build_opener()
opener.addheaders =  [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
urllib.request.install_opener(opener)
imagePath = ['https://bestoshare.com/server/php/files/19_2_general/1809091541272c2d72c6cdcd87f4d9ef.jpg',
'https://bestoshare.com/server/php/files/16_1_general/180907010237a3b8aba93ee5b866c197ab1c.JPG'
]

for eachImagePath in imagePath:
    print(eachImagePath)
    response = requests.get(eachImagePath, stream=True)
    file = BytesIO(response.content)
    predictions, probabilities = prediction.predictImage(file, result_count=5, input_type='stream')

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)


# Reverse search image by imageURL and BeautifulSoup

    googlePath = 'http://images.google.com/searchbyimage?image_url='+eachImagePath
    
    request  = urllib.request.urlopen(googlePath)
    response = request.read()
    soup = BeautifulSoup(response, 'html.parser')
    soup.prettify()
    tag = soup.find('input',attrs={"class":"gLFyf gsfi", "maxlength":"2048", "type": "text"})
    print(tag.get('value'))
    print("-------------------------------------------------------------")