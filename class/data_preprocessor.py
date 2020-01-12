import math
import numpy as npy
import pandas as pan

class DataPreprocessor():

	def __init__(self, fileName, split, columns, delimiter):
		frame = pan.read_csv(fileName, delimiter=delimiter)
		i_split = int(len(frame) * split)
		self.data_train = frame.get(columns).values[:i_split]
		self.data_test  = frame.get(columns).values[i_split:]
		self.len_train  = len(self.data_train)
		self.len_test   = len(self.data_test)
		self.len_train_windows = None

