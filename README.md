# complaint-classification-app

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
