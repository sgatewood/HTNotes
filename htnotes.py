import sys
import re

argc = len(sys.argv)
if argc != 2:
	print("Usage: htnotes.py file.htn")
	exit()

filename = sys.argv[1]

with open(filename) as y:
	lines = y.readlines()

out = open("out.html","w")
def write(string):
	# print(string)
	print(string,file=out)


def setup():
	out = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
	<head>
		<meta charset="utf-8">
		<title></title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
		<script src="htnotes.js"></script>
		<link rel="stylesheet" href="htnotes.css">
	</head>
<body>
	"""
	write(out)

def teardown():
	write("</body>\n</html>")

colors = ["black","blue","green","brown"]
last_tab_level = 0
def print_div(line,tabs):
	global last_tab_level
	font_size = 50 - 7*tabs
	margin_left = tabs * 3
	color = colors[tabs % len(colors)]
	style = "font-size: %rpx;margin-left: %r%%;color: %s;" %(font_size,margin_left,color)
	out = ("\t" * (tabs + 1)) + "<div class='node' level=%r style='%s'> %s </div>" %(tabs,style,line)
	write(out)
	# write("\t" * (tabs + 1) + "<div class='container' level='%r'>" %tabs)





setup()
for line in lines:
	tabs = 0
	while line[0] == "\t":
		tabs += 1
		line = line[1:]
	print_div(line.strip(),tabs)
teardown()
out.close()
