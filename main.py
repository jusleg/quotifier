import sys
import json
import random
import io
import os
# One more thing - Bing Han

def random_modulo():
  return random.randint(5,15)

def gen_quote():
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Kane
  random_author = random.randint(0,len(author)-1)
  random_quote = random.randint(0,len(bajson_quotes)-1)
  return bajson_quotes[random_quote] + " - " + author[random_author]
                                                      
def write_file(stringy_string,namy_name):
# The richest man is not he who has the most, but he who needs the least. - Soulja Boy
	os.remove(namy_name)
	text_file = open(namy_name, "w")
	text_file.write(stringy_string)
	text_file.close()
      
# Snow mexicans, you're getting a wall too! - Undertaker
def do_the_whole_shabang(filename):
  counter = 0
  modulo = random_modulo()
  full_file = ""
  for line in open(filename):
# It's not a muslim ban - Ch@tM@n
    counter += 1
    full_file = full_file + line
    if (counter % modulo == 0):
    	full_file = full_file + smajson[filename[filename.index('.')+1:]] + " " + gen_quote() + "\n"
  write_file(full_file,filename)
# What is a private email server? - Operah Winfrey

def smajson():
	return {"java":"//","py":"#","rb":"#","cpp":"//","tex":"%","js":"//","o":"#"}

def author():
# YES we can - Sarah Palin
	return ["Ivanka Trump","Undertaker","John Cena","Triple H","Kane","Big Show","The Rock","Bing Han","Big Cass","Sarah Palin","Dj Khaled","21 Savage","Sugar Ray Robinson","Soulja Boy","Betsy DeVos","The Red Power Ranger","Operah Winfrey","W@rri0r"]

def bajson_quotes():
	return [             
	  "The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real."
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Betsy DeVos
	  ,"I love hookers and blow."
	  ,"You can do anything, but not everything."
	  ,"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."
	  ,"The richest man is not he who has the most, but he who needs the least."
	  ,"You miss 100 percent of the shots you never take."
# I love hookers and blow. - Dj Khaled
	  ,"Courage is not the absence of fear, but rather the judgement that something else is more important than fear."
	  ,"You must be the change you wish to see in the world."
	  ,"When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean."
	  ,"To the man who only has a hammer, everything he encounters begins to look like a nail."
	  ,"We are what we repeatedly do; excellence, then, is not an act but a habit."               
# One more thing - The Rock
	  ,"We Gucci fam \n -Ghandi"           
	  ,"You must be the change you wish to see in the world."
	  ,"The weak can never forgive. Forgiveness is the attribute of the strong."
	  ,"Happiness is when what you think, what you say, and what you do are in harmony."
	  ,"An eye for eye only ends up making the whole world blind."
# First they ignore you, then they laugh at you, then they fight you, then you win. - John Cena
	  ,"Live as if you were to die tomorrow; learn as if you were to live forever."
	  ,"First they ignore you, then they laugh at you, then they fight you, then you win."
	  ,"You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty."
	  ,"The best way to find yourself is to lose yourself in the service of others."
	  ,"Strength does not come from physical capacity. It comes from an indomitable will."
# It's local on the the remote server - Soulja Boy
	  ,"A man is but the product of his thoughts; what he thinks, he becomes."
	  ,"YES we can"
	  ,"No we can't"
	  ,"Those were alternative facts"
	  ,"Don't force me to give you the D"
# Those were alternative facts - Undertaker
	  ,"You can't see me"
	  ,"I have a dream"
	  ,"In god we trust"
	  ,"Thou shall not pass"
	  ,"What is a private email server?"
# An eye for eye only ends up making the whole world blind. - Operah Winfrey
	  ,"It's local on the the remote server"
	  ,"It's not a muslim ban"
	  ,"Snow mexicans, you're getting a wall too!"
	  ,"Don't ever play yourself"
	  ,"Just play. Have fun. Enjoy the game."
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Famingo
	  ,"'Sexy' is being independent, being confident and having fun."
	  ,"It's kind of fun to do the impossible."
	  ,"We gucci Fam - Ghandi"
	  ,"I want my world to be fun."
	  ,"Everyone gets a car"
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - Ch@tM@n
	  ,"One more thing"
	  ,"Wrong"
	  ,"Such a nasty woman"
	  ,"Bazinga!"
	  ,"You shall not pass!"
	  ,"Wingardium leviosa"
	]
# We are what we repeatedly do; excellence, then, is not an act but a habit. - W@rri0r

smajson = smajson()
author = author()
bajson_quotes = bajson_quotes()
                                                      
# Wrong - Sarah Palin
if (len(sys.argv) > 1):
  do_the_whole_shabang(sys.argv[1])
