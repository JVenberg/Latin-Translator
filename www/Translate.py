#coding=utf-8
import subprocess
import re

translate_in = file("LatinIn.txt", "r")
input = translate_in.read()

input = input.replace("ā", "a")
input = input.replace("ē", "e")
input = input.replace("ī", "i")
input = input.replace("ō", "o")
input = input.replace("ū", "u")
input = input.replace(",", "")
input = input.replace(".", "")
input = input.replace(";", "")
input = input.replace("“", "")
input = input.replace("”", "")

p = subprocess.Popen([".www/words",input], stdout=subprocess.PIPE, cwd="./www")
(output, err) = p.communicate()

print output
