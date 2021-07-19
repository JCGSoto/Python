# -*- coding: utf-8 -*-
"""
My watercolor

@author: JCGS
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
stopwords=set(STOPWORDS)

qualities='Responsable Atento Puntual Alegre Curioso Apasionado Constante Motivado Python SQL Data Science Ciencia Estructutas Data Structurs MongoDB Disciplina Constacia Data Analytics Real World proyects Amazon Web Services Deep Learning TensorFlow MySQL Machine Learning Numpy Pandas MAtplotlib Python Developer FFT Vibrations Acoustics Signals Line Plot Bar Plot Box Plot Histogram Area Plot Scatter Plot Pie Chart Plot Formatting Data Frame Shape Statistics Descriptive Analysis Dashboard'

wordcloud=WordCloud(width=1000,height=500,stopwords=stopwords).generate(qualities)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')
