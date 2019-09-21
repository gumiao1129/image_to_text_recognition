# image_to_text_recognition
- Implemented by google reverse image search and artificial intelligence technologies
<ul>
<li>
1,Google Reverse image Search
</li>
Fetch image info by image search on google
<li>
2,Image Prediction
</li>
Refer <a href="https://github.com/OlafenwaMoses/ImageAI">imageAI</a> 
Suppport four algorithm and click download traiing modules<br>
1. <a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/squeezenet_weights_tf_dim_ordering_tf_kernels.h5" >SqueezeNet </a><br>
2. <a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_weights_tf_dim_ordering_tf_kernels.h5">ResNet50 by Microsoft Research</a><br>
3. <a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5">InceptionV3 by Google Brain team</a><br>
4. <a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5">DenseNet121 by Facebook AI Research</a>
</ul>

#Installation
 - Python 3.5.1 (and later versions) (Support for Python 2.7 coming soon
 - Tensorflow 1.4.0 (and later versions)
 - OpenCV 
 - Keras 2.x 
```bash
pip install -U tensorflow keras opencv-python
```
 - imageai 
```bash
pip3 install imageai --upgrade
```
 - requests
```bash
pip3 install requests
```
 - beautifulsoup4
 ```bash
pip3 install beautifulsoup4
```
#Example
Run example under folder ".\src\auto_prediction_google_AI.py" by commend line:
```bash
python .\src\auto_prediction_google_AI.py
```

