# -*- coding: utf-8 -*-
"""Blockchain_Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Suz37esxYYX7HisHdhxsb6RYgxwaQUWQ
"""

import pandas as pd


df = pd.read_csv('transactions.csv')


print(df.columns)

import pandas as pd

def load_data():

    data = pd.read_csv('transactions.csv')
    return data

data = load_data()
data.head()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder


df = pd.read_csv('transactions.csv')

print(df.head())
print(df.info())
print(df.describe())

df = df.dropna()

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(df[['customerDevice', 'customerIPAddress', 'customerBillingAddress']]).toarray()
X = np.hstack((X_encoded, df[['No_Transactions', 'No_Orders', 'No_Payments']]))
y = df['Fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)
lr_precision = precision_score(y_test, lr_pred)
lr_recall = recall_score(y_test, lr_pred)
lr_f1 = f1_score(y_test, lr_pred)

print('Logistic Regression Model Performance:')
print(f'Accuracy: {lr_accuracy:.2f}')
print(f'Precision: {lr_precision:.2f}')
print(f'Recall: {lr_recall:.2f}')
print(f'F1-score: {lr_f1:.2f}')


rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)


rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)

print('Random Forest Model Performance:')
print(f'Accuracy: {rf_accuracy:.2f}')
print(f'Precision: {rf_precision:.2f}')
print(f'Recall: {rf_recall:.2f}')
print(f'F1-score: {rf_f1:.2f}')

import hashlib
import json
from time import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, transactions: List[dict], nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time(), [])
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          previous_hash=last_block.hash,
                          timestamp=time(),
                          transactions=self.pending_transactions)


        while not new_block.hash.startswith('0000'):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder
import hashlib
import json
from time import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, transactions: List[dict], nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time(), [])
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          previous_hash=last_block.hash,
                          timestamp=time(),
                          transactions=self.pending_transactions)


        while not new_block.hash.startswith('0000'):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

df = pd.read_csv('transactions.csv')

print(df.head())
print(df.info())
print(df.describe())

df = df.dropna()

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(df[['customerDevice', 'customerIPAddress', 'customerBillingAddress']]).toarray()
X = np.hstack((X_encoded, df[['No_Transactions', 'No_Orders', 'No_Payments']]))
y = df['Fraud']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

blockchain = Blockchain()

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)
lr_precision = precision_score(y_test, lr_pred)
lr_recall = recall_score(y_test, lr_pred)
lr_f1 = f1_score(y_test, lr_pred)

print('Logistic Regression Model Performance:')
print(f'Accuracy: {lr_accuracy:.2f}')
print(f'Precision: {lr_precision:.2f}')
print(f'Recall: {lr_recall:.2f}')
print(f'F1-score: {lr_f1:.2f}')

transaction = {
    'model': 'Logistic Regression',
    'accuracy': lr_accuracy,
    'precision': lr_precision,
    'recall': lr_recall,
    'f1_score': lr_f1,
    'timestamp': time()
}
blockchain.add_transaction(transaction)
blockchain.mine_block()


rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)


rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)

print('Random Forest Model Performance:')
print(f'Accuracy: {rf_accuracy:.2f}')
print(f'Precision: {rf_precision:.2f}')
print(f'Recall: {rf_recall:.2f}')
print(f'F1-score: {rf_f1:.2f}')

transaction = {
    'model': 'Random Forest',
    'accuracy': rf_accuracy,
    'precision': rf_precision,
    'recall': rf_recall,
    'f1_score': rf_f1,
    'timestamp': time()
}
blockchain.add_transaction(transaction)
blockchain.mine_block()

for block in blockchain.chain:
    print(f'Index: {block.index}, Hash: {block.hash}, Transactions: {block.transactions}')