## Machine Learning Pipeline for Prediction using Modular Approach



This project implements a complete machine learning pipeline designed to predict students' math scores using a modular approach. The workflow includes data collection, preprocessing, feature engineering, and model training. Several machine learning models are trained, followed by hyperparameter tuning to optimize their performance. The model that achieves the highest accuracy is selected for making predictions on new data. The approach emphasizes flexibility, allowing each step of the pipeline to be independently modified or improved as needed. The project demonstrates how to handle real-world datasets and build a robust machine learning solution from data ingestion to model evaluation. Also, the project includes a web interface created using Flask. By converting the machine learning pipeline into an API, users can input student data directly through a web form and receive predicted math scores in real-time, making the process accessible and interactive.



The primary focus of this project is to build a flexible and reusable machine learning pipeline where each step, from data preprocessing to model evaluation, is organized in separate, independent modules. This approach ensures that the workflow can be easily extended, modified, or reused for similar tasks.

#### Dataset
The dataset consists of several features related to student demographics and academic performance:

1- gender: Gender of the student (male/female)

2- race_ethnicity: Ethnic group of the student

3- parental_level_of_education: Highest level of education achieved by the student's parent(s)

4- lunch: Type of lunch received by the student (standard or free/reduced)

5- test_preparation_course: Whether the student completed a test preparation course (none/completed)

6- reading_score: The student's reading test score

7- writing_score: The student's writing test score




The target variable to be predicted is: 
math_score: The student's math test score
