#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(',')[2].split(' ')[0]+ ' ' + ' ' + str.split(',')[2].split(' ')[1] + ' ' + str.split(',')[2].split(' ')[2]+ ' ' + str.split(',')[2].split(' ')[8]+ ' ' + str.split(',')[0].split(' ')[0]
print(str)
