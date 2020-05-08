# Basic packages
import pandas as pd 
print('pandas: %s' % pd.__version__)
import numpy as np
import re
import collections
import time
#import matplotlib.pyplot as plt



# Packages for data preparation
from sklearn.model_selection import train_test_split,StratifiedKFold, cross_val_score
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.utils.np_utils import to_categorical
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import average_precision_score, precision_recall_curve, confusion_matrix

# Packages for modeling
from keras import models
from keras import layers
from keras import regularizers

# Word cloud visualization libraries
#rom scipy.misc import imresize
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from collections import Counter

import itertools

from keras.wrappers.scikit_learn import KerasClassifier

# Packages for Sequence and CNN based layers
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential, Model, load_model
from keras.layers.embeddings import Embedding
from keras.layers import Flatten, Dense, Dropout, AlphaDropout, ThresholdedReLU, Convolution1D, ZeroPadding1D, Activation, MaxPooling1D, SpatialDropout1D, Input 
from keras.layers import GlobalMaxPooling1D, concatenate, LSTM, Bidirectional,BatchNormalization
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint, EarlyStopping,TensorBoard