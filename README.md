**Telco Classfication Project**

**Project Objectives**

- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook Final Report.

- Create modules (acquire.py, prepare.py) that make your process repeateable and your report (notebook) easier to read and follow.

- Ask exploratory questions of your data that will help you understand more about the attributes and drivers of customers churning. Answer questions through charts and statistical tests.

- Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers.

- Refine your work into a Report, in the form of a jupyter notebook, that you will walk through in a 5 minute presentation to a group of collegues and managers about the work you did, why, goals, what you found, your methdologies, and your conclusions.

- Be prepared to answer panel questions about your code, process, findings and key takeaways, and model.

**Business Goals**

- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn.

- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

**Audience**

-Your target audience for your notebook walkthrough is your direct manager and their manager. This should guide your language and level of explanations in your walkthrough.

**Deliverables**

You are expected to deliver the following:

Github repo with the following:

- Readme (.md)

- project description with goals

- initial hypotheses and/or questions you have of the data, ideas

- data dictionary

- project planning (lay out your process through the data science pipeline)

- instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

- key findings, recommendations, and takeaways from your project.

- Final Report (.ipynb) (see details above in the "Jupyter Notebook Report"

- A Report that has filtered out all the extraneous elements not necessary to include in the report.


- Include at least 4 visualizations in the form of:

   - Question in markdown that you want to answer

   - visualization

   - statistical test (in at least 2 of your 4)


- Include your 3 best models in the final notebook to review. Show the steps and code you went through to fit the models, evaluate, and select.


- Acquire & Prepare Modules (.py)


- A Predictions (.csv).

   - 3 columns: customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn).


- 1+ non-final Notebooks (.ipynb) created while working on the project, containing exploration & modeling work (and other work)

- Live Presentation


**Execuitve Summary**
- Key Findings: Drivers of churn are family types, payment type, fiber optic internet, and add-on services.


- Recommendations: 
    - Offer senior citizen discounts
    - strategize marketing to younger families
    - discourage use of electronic checks (incenvtivize other payment options)
    - offer discounts for bundled add-on services with Fiber Optic internet.

- Multiple models were created, fit, and evaluated. 
    - Logistic Regression was chosen as the best model as its accuracy was above baseline and the recall rate was the highest of all the other models. This model performed at 75% accuracy with a recall rate of 79% on the positive case.


**Plan**
 - Questions to answer:
    - Does contract type matter?
    - Do those that churn pay more?
    - Does family type drive churn rates?
        -Explore gender, senior citizens, customers with dependents and partners.
    - Does payment type matter?
    - Does phone type or internet type lead to churn?
    - How do add-on services affect churn?

**Acquire**
- utlize acquire.get_telco_data() to gain acces to the telco dataset.

**Prepare**
- utilize prepare.clean_telco_data() to remove unneccesary columns, utilize one-hot encoding, remove nulls, and change datatypes in order to utilize data effectively within the models.
- utilize prepare.prep_telco_data() to split the dataset into train, validate, and test datasets.

**Explore**
- exploratory analysis of the train dataset to answer the previously asked questions via visulaizations and statistic analysis.

**Model**
- create multiple classification models to include decision trees, random forests, K-nearest neighbors, and logistic regression.
- fit, evaluate, and select the best performing model.
- test the BEST model on the test dataset.


**Project Reproduction**
- In order to reproduce this project you will need your own .env file with Codeup database credentials, as well as:
   - jupyter notebook
   - acquire.py
   - prepare.py
   - Classification Project - Final.ipynb
