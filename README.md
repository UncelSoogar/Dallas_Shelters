# Gimme Shelter
## An analyis of Dallas Animal Service's shelter intake and predictive outcomes.
---
### ABSTRACT
The focus of this project was to analyze the Dallas OpenData spreadsheets from January 2015 – August 2020 and to explore the outcome of the animals that enter the Dallas Shelter and their location. The dataset included over 200,000 animals. This dataset was filtered down to eliminate non-viable animals, (dead on arrival, or both found untreatable and contagious), also the animals that are recorded in the shelter for over 60 days. The data was later analyzed and visualized using the tools provided by Tableau. To make the predictive models, the data was divided into cats and dogs and then built using SciKit-Learn’s ‘Gradient Boost Classifier’ so they can predict live models on the chosen values by users.

### Table of Contents
- [Live Deployment](https://dallas-shelter.herokuapp.com/)
- [Written Report](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/GimmeShelterReport.pdf)
- Cleaning and Modeling Notebooks
  - [Data Cleaning Notebook](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Notebooks/data_clean.ipynb)
  - [Dog Predictive Model Testing](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Notebooks/dog_ml.ipynb)
  - [Cat Predictive Model Testing](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Notebooks/cat_ml.ipynb)
  - [Testing Saved Models and Scalers](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Notebooks/model_testing.ipynb)
- Cleaned Data Tables
  - [Combined Animal Data](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Resources/combined_shelter_data.csv)
  - [Filtered Dog Data](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Resources/dog.csv)
  - [Filtered Cat Data](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/Resources/cat.csv)
 - [Flask App](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/html/app.py)
- [Python Libraries and Versions Used](https://github.com/UncelSoogar/Dallas_Shelters/blob/master/html/requirements.txt)


#### This app was designed and developed with the help of:
- [Ana Gill](https://github.com/anag33)
- [Chris Krokus](https://github.com/chris-krokus)
- [Christion Lankford](https://github.com/Chriztion)

*Source data from [Dallas OpenData](https://www.dallasopendata.com/browse?q=animal+shelter)*
