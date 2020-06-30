# Este script converte um documento de texto em HTML para
# um documento de texto em ASCII (transforma os caracteres
# reservados HTML para as devidas sequências) para ser
# inserido como texto no documento HTML, e mostrado corre-
# tamente na página.
# > Utilização: python ascii_to_html.py input_filename output_filename

# ~~~~~~~~~~~~~~~~~~~~~~ X ~~~~~~~~~~~~~~~~~~~~~~ X ~~~~~~~~~~~~~~~~~~~~~~
# Para adicionar cores ao texto, ative a variável abaixo, e adicione
# as tags que achar necessário:

text_colors = True
comment_color = "grey"
tag_color = "yellow"
tags = [
	"<!DOCTYPE html>", 
	"<html>", "</html>",
	"<html lang=\"en\">", 
	"<html lang=\"pt-br\">", 
	"<head>", "</head>",
	"<title>", "</title>",
	"<body>","</body>",
	"<h1>", "</h1>",
	"<p>", "</p>",
	"<script>","</script>",
	]

# ~~~~~~~~~~~~~~~~~~~~~~ X ~~~~~~~~~~~~~~~~~~~~~~ X ~~~~~~~~~~~~~~~~~~~~~~

import sys

input_filename, output_filename = sys.argv[1], sys.argv[2]

def loadtext(file):
	f = open(file, "r")
	text = f.read()
	f.close()
	return text

keywords = {
	"\t" : "&emsp;",
	"&" : "&#38;",
	"<" : "&#60;",
	">" : "&#62;",
	"\n" : "<br>",
}

def span_color(color, text):
	new_text = "<span style=\"color: " + color + "\">" + text
	return new_text

def change_tags():
	for key in keywords:
		for i, _ in enumerate(tags):
			tags[i] = tags[i].replace(key, keywords[key])

def insert_colors(text):
	change_tags()
	# Comentários:
	text = text.replace("&#60;!--", span_color(comment_color, "&#60;!--"))
	text = text.replace("--&#62;", "--&#62;" + "</span>")
	# Tags:
	for tag in tags:
		text = text.replace(tag, span_color(tag_color, tag) + "</span>")
	return text

def ascii_to_html(input_filename, output_filename):
	w = open(output_filename, "w")
	text = loadtext(input_filename)
	for word in keywords: 
		text = text.replace(word, keywords[word])
	if(text_colors): text = insert_colors(text)
	# print(text) # Debugging
	w.write(text)
	w.close()

ascii_to_html(input_filename, output_filename)