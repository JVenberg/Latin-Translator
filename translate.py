#coding=utf-8
from lxml import html
import requests
import re
class Translator(object):
	"""docstring for Translator"""
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
		
	def request_translation(self, input):
		self.input = self.remove_useless(input)
		words = input.split()
		page = requests.get('http://www.archives.nd.edu/cgi-bin/wordz.pl?keyword='+ "+".join(words))
		tree = html.fromstring(page.text)
		translation = tree.xpath('//pre/text()')
		translations = translation[0].split('\n\n')
		#m = re.search('(?<=(\]  \n))(.*?)$', translations[0])
		#print m.group(0)
		return translations

	def print_translation(self, input):
		self.translations = self.request_translation(input)
		for word in self.translations:
			print word + "\n\n"