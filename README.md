# TECHTonic Tracer
## Overview
TECHTonic Tracer is a website that leverages machine learning to predict earthquakes before they occur.

## Quick Start
You will firstly need to install the dependencies with

`pip install -r requirements.txt`

After that, you will need to generate a google map api token on Google Cloud and store it in configure file.

Ultimately, run the program on port 5000 with

`python run.py`

And you are all set!

## Significance
Currently, seismologists do not have a dependable tool to predict major earthquakes as they continue to have major, disastrous impacts worldwide. 

Although there have been attempts to use classic neural networks as a way to address this issue, they fail to consider examples of when earthquakes do not happen during supervised training. If modeled as a classification problem, the model then runs with a multi-class classifier on positive examples only, resulting in inaccurate results.

To mitigate this issue, we model our problem as a regression task with the earthquake’s magnitude being the output and use data augmentation to generate and represent data for when the earthquakes are insignificant or do not occur at all. We set a range of -100 to -10 for those magnitudes.

For the model, we used Microsoft’s AutoML to select the most powerful model for our dataset, instead of selecting one ourselves. AutoML used LightGBM to train our models. 

We have also cleaned the original dataset to extract the needed features. The dataset covers registered earthquakes around the world from 1970 to March 2019, with the earthquake data obtained from the USGS.

## Usage and Functionality
Users can input the date, time, location (longitude and latitude) of the earthquake they wish to predict through the website's user interface. The website then uses a trained model to provide a prediction in terms of magnitude, along with an interpretation of the prediction, which can be categorized as major, minor, very little, or no earthquake foreseen. Additionally, the website has input validation to ensure that incorrect or missing inputs are detected and corrected.

## Extensions
Due to time constraints, we downsampled the total dataset to 100,000 examples. Using a larger dataset to improve accuracy is one future extension. We also think using more features relevant to earthquakes would improve accuracy. 

## Running and Navigating the Project
Make sure to pip install geocoder, pickle5, and flaml. M1 users might also need to brew install cmake libomp. Run python3 run.py in the Flask directory to run the code for the website. 

All code for the website is in the Flask directory. The other directory contains files used for training and testing the model as well as the script for data augmentation.  

## Fun Facts:
Wanna see if the tectonic plates are doing alright? TECHtonic tracer has got you covered! Pun intended ;)

## UI
All parts of our UI are designed and handdrawn by our awesome front end developer Emily! See the design plan and assets in figma below. 
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FJXUG6ofcTSLNL0lntgDYIy%2FTECHtonic-Tracer%3Fnode-id%3D0%253A1%26t%3DnGGNT2caVl54QFxZ-1" allowfullscreen></iframe>

