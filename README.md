# 
<h1 align="center">Complaint Classification App

</h1>




<br>
 <p><div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" /> <!-- line breaker --></p></div>

<!--- header ---->
  
## ABOUT
  - This model will analyze complaints and classify them into different categories like Credit reporting, Debt collection and Mortgages and loans ...etc
  - It could be used to streamline the routing and processing of incoming messages for an organization and can simplify the complaint-submission process for consumers.
  - The dataset is collected from Consumer Financial Protection Bureau (CFPB)
  - The Consumer Financial Protection Bureau (CFPB), a federal agency that began operations only in 2011, looks after the interests of consumers in the financial sector. As part of that mission, consumers can send in complaints when they feel they’ve been mistreated by a credit bureau, a bank, a credit card company, or another financial service provider.

## FILES AND DIRECTORIES
- complaint-classification-app/model_building/model_building.ipynb - `notebook contains text preprocessing, text encoding and models evaluation and model selection for all classifiers (product, sub-product, issue, sub-issue)`

* results.csv - `all requests and their responses in csv format`

* utils.py - `contains the models and encoders config's and utility functions for prediction and creating response`

## LOCAL TEST
```bash

pip install -r requirements.txt

python app.py
```
after visit :- http://127.0.0.1:8000/docs


## DEPLOYMENT
- API created by using FastAPI
- API deployed in heroku

API FOR COMPLAINT CLASSIFICATION
```bash
curl -X 'POST' 'https://complaint-classifcation.herokuapp.com/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"complaint": "your complaint" }' 
```

RESPONSE FORMAT
```json
{
  "product" : "Credit reporting",
  "sub_product" : "Credit reporting",
  "issue" : "Improper use of your report",
  "sub_issue":"Credit inquiries on your report that you don't recognize"
}

```

  
 <!--- footer --->
 <div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" /> <!-- line breaker -->
<p>

 <a href="https://www.linkedin.com/in/adil-rahman-80b17a23a/"  >connect with me</a><br><br>
<a href="https://www.linkedin.com/in/adil-rahman-80b17a23a/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a> <a href="https://www.instagram.com/___i_am_iron_man/?hl=en" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a> <a href="https://twitter.com/bitbyte_1337" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="DEV.to"></a> <a href="https://medium.com/@adilrahman_1337" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="DEV.to"></a>

</p>
</div>
