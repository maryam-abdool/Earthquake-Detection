# TECHTonic Tracer
## Overview
TECHTonic Tracer is an earthquake predictor (website) that uses machine learning to warn people about future earthquakes before they happen.

## Significance
Currently, seismologists do not have a dependable tool to predict major earthquakes as they continue to have major, disastrous impacts worldwide. 

Although there have been attempts to use classic neural networks as a way to address this issue, they fail to consider examples of when earthquakes do not happen in their supervised training. If modeled as a classification problem, the model then runs with a multi-class classifier on positive examples only, resulting in inaccurate results.

To mitigate this issue, we model our problem as a regression task with the earthquake’s magnitude being the output and use data augmentation to generate and represent data for when the earthquakes are insignificant or do not occur at all. We set a range of -100 to -10 for those magnitudes.

For the model, we used Microsoft’s AutoML to select the most powerful model for our dataset, instead of selecting one ourselves. AutoML used LightGBM to train our models. 

We have also cleaned the original dataset to extract the needed features. The dataset covers registered earthquakes around the world from 1970 to March 2019, with the earthquake data obtained from the USGS.

## Usage and Functionality
The user will provide the date, time, and location of the earthquake they wish to predict (inputted as the longitude and latitude) through the UI, and the website will return the model’s prediction in terms of the magnitude and an interpretation — major, minor, very little or no earthquake foreseen. The website also provides input validation for incorrect or missing inputs.

## Extensions
Due to time constraints, we downsampled the total dataset to 100,000 examples. Using a larger dataset to improve accuracy is one future extension. We also think using more features relevant to earthquakes would improve accuracy. 

## Running and Navigating the Project
Make sure to pip install geocoder, pickle5, and flaml. M1 users might also need to brew install cmake libomp. Run python3 run.py in the Flask directory to run the code for the website. 

All code for the website is in the Flask directory. The other directory contains files used for training and testing the model as well as the script for data augmentation.  

## Fun Facts:
Pun intended ;)

## UI
All parts of our UI are drawn by our awesome designer! See the screenshots below. 
