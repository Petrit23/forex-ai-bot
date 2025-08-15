import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib
import os

MODEL_PATH = "model.joblib"

def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def preprocess_data(df):
    df["return"] = df["close"].pct_change().fillna(0)
    df["ma_fast"] = df["close"].rolling(5).mean().fillna(method='bfill')
    df["ma_slow"] = df["close"].rolling(20).mean().fillna(method='bfill')
    df["ma_cross"] = (df["ma_fast"] > df["ma_slow"]).astype(int)
    features = df[["return", "ma_cross"]].values
    return features

def make_trade_decision(df):
    if df["ma_cross"].iloc[-1] == 1 and df["ma_cross"].iloc[-2] == 0:
        return 1  # BUY
    elif df["ma_cross"].iloc[-1] == 0 and df["ma_cross"].iloc[-2] == 1:
        return -1 # SELL
    else:
        return 0  # HOLD

def ai_decision(df):
    model = load_model()
    if model is None:
        return make_trade_decision(df)
    X = preprocess_data(df)
    pred = model.predict([X[-1]])
    return pred[0]

def train_on_historical(df):
    df = df.copy()
    df["target"] = 0
    df.loc[df["return"] > 0.001, "target"] = 1
    df.loc[df["return"] < -0.001, "target"] = -1
    X = preprocess_data(df)
    y = df["target"].values
    train_model(X, y)
