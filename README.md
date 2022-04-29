# Accenture_AI_SPY
## How to use it
![Image Caption Generator] (https://image-desc111.azurewebsites.net/)
### Paste an image link

The web app requires an image link to be pasted in a text box by copying an image from the internet (right-click, copy image link), whereafter it is inserted in the textbox, the user can click on **Get Caption**. 

![alt text](https://github.com/okayshahi/Accenture_AI_SPY/blob/master/static/index%20image.png)

### Results 
After which, the user will be redirected to the caption generated results. This result page shows the user the caption, its confidence as well as image tags associated with the image. If the image contains a celebrity, Accenture_AI_SPY can include them in the caption as well.

![alt text](https://github.com/okayshahi/Accenture_AI_SPY/blob/master/static/Dog.png)

## How I built it
The web app was built using the Computer Vision Cognitive Service and the App Service from Azure using the APIs. The Flask framework was used to create the web development along with the programming language in Python which was all implemented through the VS code IDE.

## How to run locally
Clone this project using the command line in bash

```bash
git clone https://github.com/okayshahi/Accenture_AI_SPY.git
```
Set up the virtual envinroment

```
python -m venv venv
```

Activate virtual environment for Windows

```
venv\Scripts\activate
```

Activate virtual environment for macOS / Linux

```
source ./venv/bin/activate
```

Install flask with other libraries

```
pip install -r requirements.txt
```
Run the flask app

```
flask run
```

