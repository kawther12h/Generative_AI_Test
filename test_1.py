# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NNYtt3NsuK_Na8mQJNptQEjqtG0eVzpE
"""

# Load a specific model for sentiment analysis
classifier = pipeline('sentiment-analysis', model='PRAli22/AraBert-Arabic-Sentiment-Analysis')
sentence = "هذة أسوء تجربة"
result = classifier(sentence)
output=result[0]
print(output)
print(output["label"])
print(output["score"])