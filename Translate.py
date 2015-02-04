#coding=utf-8
from lxml import html
import requests
import re
class Translate(object):
	"""docstring for Translate"""
	def __init__(self):
		pass
	def remove_useless(self, input):
		self.input = input
		self.input = self.input.replace("ā", "a")
		self.input = self.input.replace("ē", "e")
		self.input = self.input.replace("ī", "i")
		self.input = self.input.replace("ō", "o")
		self.input = self.input.replace("ū", "u")
		self.input = self.input.replace(",", "")
		self.input = self.input.replace(".", "")
		self.input = self.input.replace(";", "")
		self.input = self.input.replace("“", "")
		self.input = self.input.replace("”", "")
		return self.input

