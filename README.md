# RainfallEstimation
Lab project
This project aims to improve rainfall estimates in northern Vietnam using infrared satellite data
The idea is based on this paper: https://www.jstage.jst.go.jp/article/jmsj/97/3/97_2019-040/_article 



# Guideline
1. Running RFE.py to have the labels ranking using Recursive Feature Elimination method (output is saved to cls_FRE.xlsx file)
2. Running Classification/TestSplit.ipynb file to split the data into training and testing dataset 
NOTE: The data is too large and not for public view so if you have any interest you can contact me via email 'ngpminhanh2511@gmail.com"
3. Running Classication/RandomForestClassification.ipynb to view first two model 
    - Model to classify rain and dry area
    - Model to classify weak and strong rain 
4. Running StatisticalDataAnalysis.ipynb to have an EDA view about the data 



# Short introduction about the dataset using for the project
- The dataset contains values being extracted from Himawari-8 AHI IR bands (individuals and mix bands) and weather station of full days and hours data in 2019 and 2020 
- Values from weather station is considered as groundtruth value

