import pickle
import pandas as pd
from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import contractions
import warnings
import nltk

warnings.filterwarnings("ignore")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
## models and  encoders path

#product
PRODUCT_PREDICTION_MODEL_PATH = "models/product_model.pkl"
PRODUCT_Y_LABEL_ENCODER_PATH = "encoders/product_encoder.pkl"
PRODUCT__TF_IDF_TRANSFORMER_PATH = "encoders/product_tf_idf_vectorizer.pkl"

# sub product
SUB_PRODUCT_PREDICTION_MODEL_PATH = "models/sub_product_model.pkl"
SUB_PRODUCT_Y_LABEL_ENCODER_PATH = "encoders/sub_product_encoder.pkl"
SUB_PRODUCT_TF_IDF_TRANSFORMER_PATH = "encoders/sub_product_tf_idf_vectorizer.pkl"

#issue
ISSUE_PREDICTION_MODEL_PATH = "models/issue_model.pkl"
ISSUE_Y_LABEL_ENCODER_PATH = "encoders/issue_encoder.pkl"
ISSUE_TF_IDF_TRANSFORMER_PATH = "encoders/issue_tf_idf_vectorizer.pkl"

#sub issue
SUB_ISSUE_PREDICTION_MODEL_PATH = "models/sub_issue_model.pkl"
SUB_ISSUE_Y_LABEL_ENCODER_PATH = "encoders/sub_issue_encoder.pkl"
SUB_ISSUE_TF_IDF_TRANSFORMER_PATH = "encoders/sub_issue_tf_idf_vectorizer.pkl"

## loading models and encoders

#product
PRODUCT_PREDICTION_MODEL = pickle.load(open(PRODUCT_PREDICTION_MODEL_PATH, "rb"))
PRODUCT_Y_LABEL_ENCODER = pickle.load(open(PRODUCT_Y_LABEL_ENCODER_PATH, "rb"))
PRODUCT_TF_IDF_TRANSFORMER = pickle.load(open(PRODUCT__TF_IDF_TRANSFORMER_PATH, "rb"))

# sub product
SUB_PRODUCT_PREDICTION_MODEL = pickle.load(open(SUB_PRODUCT_PREDICTION_MODEL_PATH, "rb"))
SUB_PRODUCT_Y_LABEL_ENCODER = pickle.load(open(SUB_PRODUCT_Y_LABEL_ENCODER_PATH, "rb"))
SUB_PRODUCT_TF_IDF_TRANSFORMER = pickle.load(open(SUB_PRODUCT_TF_IDF_TRANSFORMER_PATH, "rb"))

#issue
ISSUE_PREDICTION_MODEL = pickle.load(open(ISSUE_PREDICTION_MODEL_PATH, "rb"))
ISSUE_Y_LABEL_ENCODER = pickle.load(open(ISSUE_Y_LABEL_ENCODER_PATH, "rb"))
ISSUE_TF_IDF_TRANSFORMER = pickle.load(open(ISSUE_TF_IDF_TRANSFORMER_PATH, "rb"))

#sub issue
SUB_ISSUE_PREDICTION_MODEL = pickle.load(open(SUB_ISSUE_PREDICTION_MODEL_PATH, "rb"))
SUB_ISSUE_Y_LABEL_ENCODER = pickle.load(open(SUB_ISSUE_Y_LABEL_ENCODER_PATH, "rb"))
SUB_ISSUE_TF_IDF_TRANSFORMER = pickle.load(open(SUB_ISSUE_TF_IDF_TRANSFORMER_PATH, "rb"))


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")


class TextPreprocessing:
    def __init__(self, tfidf_vectorizer, y_label_encoder) -> None:
        self.tfidf_vectorizer = tfidf_vectorizer
        self.y_label_encoder = y_label_encoder

    def preprocess(self, data):
        X = data["Consumer complaint narrative"].apply(self.text_cleaning)
        X = self.tfidf_vectorizer.transform(X)
        X = X.toarray()

        return X

    def text_cleaning(self, text: str) -> str:
        """
        description:
          it clean the text
            - change to lower case
            - remove the numerical numbers
            - remove newline symbols , special symbols, whitespace
            - transforming every tokens into it's stem form
            - expanding the contractions
        """
        text = text.lower()

        # change numerical money to 'money'
        text = re.sub("\$[0-9.]+", "dollar money", text)
        # removing the newline symbols '\n'
        text = re.sub("\n", " ", text)

        # changing format of dates
        text = re.sub("[0-9x]+/[0-9x]+/[0-9x]+", " date ", text)

        text = re.sub(r"[0-9]+", "number", text)
        text = re.sub(r"xx+", "", text)
        text = re.sub(r"[^a-zA-Z ]+", " ", text)
        text = re.sub(r"\s+", " ", text)
        text = text.lstrip().rstrip()
        tokens = self.tokenizer(sentance=text)
        #
        tokens = [
            stemmer.stem(contractions.fix(token))
            for token in tokens
            if token not in stop_words
        ]
        text = " ".join(tokens).lstrip().rstrip()

        return text

    def tokenizer(self, sentance):
        return word_tokenize(sentance)

    def y_label_decode(self, class_id: int) -> str:
        res = self.y_label_encoder.classes_[class_id]

        return res


class Model:
    def __init__(self, model, preprocessor) -> None:
        self.model = model
        self.text_preprocessor = preprocessor

    def predict(self, data: str) -> str:
        X = self.text_preprocessor.preprocess(data)
        prediction = self.model.predict(X)
        prediction = self.text_preprocessor.y_label_decode(class_id=int(prediction[0]))

        return prediction

# product
textPreprocessor = TextPreprocessing(
        tfidf_vectorizer=PRODUCT_TF_IDF_TRANSFORMER,
        y_label_encoder=PRODUCT_Y_LABEL_ENCODER,
    )

product_classifier = Model(model=PRODUCT_PREDICTION_MODEL, preprocessor=textPreprocessor)


# sub product
textPreprocessor = TextPreprocessing(
        tfidf_vectorizer=SUB_PRODUCT_TF_IDF_TRANSFORMER,
        y_label_encoder=SUB_PRODUCT_Y_LABEL_ENCODER,
    )
sub_product_classifier = Model(model=SUB_PRODUCT_PREDICTION_MODEL, preprocessor=textPreprocessor)


# issue 
textPreprocessor = TextPreprocessing(
        tfidf_vectorizer=ISSUE_TF_IDF_TRANSFORMER,
        y_label_encoder=ISSUE_Y_LABEL_ENCODER,
    )
issue_classifier = Model(model=ISSUE_PREDICTION_MODEL, preprocessor=textPreprocessor)


# sub issue
textPreprocessor = TextPreprocessing(
        tfidf_vectorizer=SUB_ISSUE_TF_IDF_TRANSFORMER,
        y_label_encoder=SUB_ISSUE_Y_LABEL_ENCODER,
    )
sub_issue_classifier = Model(model=SUB_ISSUE_PREDICTION_MODEL, preprocessor=textPreprocessor)





if __name__ == "__main__":



    complaint = input("enter the complaint : ")
    data = {
        "Consumer complaint narrative": str(complaint),
    }
    data = pd.DataFrame(data, index=[0])
    product_prediction = product_classifier.predict(data=data)
    sub_product_prediction = sub_product_classifier.predict(data=data)
    issue_prediction = issue_classifier.predict(data=data)
    sub_issue_prediction = sub_issue_classifier.predict(data=data)

    print("product : " + product_prediction)
    print("sub_product : " + sub_product_prediction)
    print("issue : " + issue_prediction)
    print("sub issue : " + sub_issue_prediction)

