# Generates a table in HTML, with all ASCII Symbols and its respectives HTML codes

file_name = "html_symbols.html"

symbols = []
html_numbers = []

a = "&#38;" # ampersand: &
h = "&#35;" # hashtag: #
s = "&#59;" # semicolon: ;

for i in range(32, 127):
	symbols.append("&#" + str(i) + ";")
	html_numbers.append(a+h+str(i)+s)

for i in range(161, 256):
	symbols.append("&#" + str(i) + ";")
	html_numbers.append(a+h+str(i)+s)

text = []

text.append("<table>\n");
# First line:
line1 = "\t<tr>"
for i in range(10): 
	line1 += " <th> HTML Code </th> <th> Symbol </th>"
line1 += " </tr>\n"
text.append(line1)
# 2nd line onwards
for lines in range(19):
	line = "\t<tr>"
	for rows in range(10):
		line += " <td> " + html_numbers[19*rows + lines] + " </td>"
		line += " <td> " + symbols[19*rows + lines] + " </td>"
	line += " </tr>\n"
	text.append(line)

text.append("</table>\n")

with open(file_name, "x") as f:
	for line in text:
		f.write(line)