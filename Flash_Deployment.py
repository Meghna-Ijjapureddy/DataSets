from flask import Flask, request, json
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from flask_cors import CORS