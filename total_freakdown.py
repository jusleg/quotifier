# Import some goodies
import sys, json, random,os

# Genereate a random number between 5 and 15
def random_modulo():
    return random.randint(5,15)

# I love hookers and blow. - Clyde Frog
# The weak can never forgive. Forgiveness is the attribute of the strong. - Betsy DeVos
# Just play. Have fun. Enjoy the game. - Sarah Palin
# Wrong - Dog The Bount Hunter
# It's not a muslim ban - Stev-o
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Soulja Boy
# You can do anything, but not everything. - Master Yoda
# The richest man is not he who has the most, but he who needs the least. - Satan
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Dj Khaled
# Genereate a random quote - by a random author
# Wrong - The Red Power Ranger
# The weak can never forgive. Forgiveness is the attribute of the strong. - Master Yoda
# We are what we repeatedly do; excellence, then, is not an act but a habit. - The Red Power Ranger
# Bazinga! - Master Yoda
# The best way to find yourself is to lose yourself in the service of others. - Satan
# I have a dream - Kane
# You can do anything, but not everything. - Dog The Bount Hunter
# Thou shall not pass - Momo Taleb
def gen_quote():
# Grab them by the pussy! - Abe Lincoln
# One more thing - Dj Khaled
# Bazinga! - Undertaker
# You must be the change you wish to see in the world. - Dog The Bount Hunter
# Happiness is when what you think, what you say, and what you do are in harmony. - Bing Han
# Snow mexicans, you're getting a wall too! - Big Show
# Strength does not come from physical capacity. It comes from an indomitable will. - Ivanka Trump
# You miss 100 percent of the shots you never take. - Oprah Winfrey
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Big Show
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Dj Khaled
# The weak can never forgive. Forgiveness is the attribute of the strong. - Sugar Ray Robinson
# 'Sexy' is being independent, being confident and having fun. - Master Yoda
# You must be the change you wish to see in the world. - Master Yoda
# You shall not pass! - Master Yoda
# 'Sexy' is being independent, being confident and having fun. - Wee-man
# It's local on the the remote server - John Cena
# 'Sexy' is being independent, being confident and having fun. - Big Show
# Don't force me to give you the D - Clyde Frog
# You must be the change you wish to see in the world. - Ivanka Trump
# Those were alternative facts - John Cena
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Kane
# We gucci Fam - Ghandi - Big Show
# One more thing - Sarah Palin
# The best way to find yourself is to lose yourself in the service of others. - Bing Han
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Undertaker
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - Wee-man
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Triple H
    random_author = random.randint(0,len(author)-1)
    random_quote = random.randint(0,len(bajson_quotes)-1)
# A man is but the product of his thoughts; what he thinks, he becomes. - Triple H
# I want my world to be fun. - The Rock
# You miss 100 percent of the shots you never take. - Triple H
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - Clyde Frog
# YES we can - Triple H
    return bajson_quotes[random_quote] + " - " + author[random_author]
# The best way to find yourself is to lose yourself in the service of others. - 21 Savage
# C++ supports OOP - Sugar Ray Robinson
# Don't ever play yourself - John Cena
# Such a nasty woman - The Rock
# One more thing - Satan
# You must be the change you wish to see in the world. - Oprah Winfrey
# You miss 100 percent of the shots you never take. - Momo Taleb
# The weak can never forgive. Forgiveness is the attribute of the strong. - Sugar Ray Robinson
# The richest man is not he who has the most, but he who needs the least. - Ivanka Trump
# Those were alternative facts - Ivanka Trump
# The best way to find yourself is to lose yourself in the service of others. - Master Splinter
# YES we can - Dog The Bount Hunter
# To the man who only has a hammer, everything he encounters begins to look like a nail. - 21 Savage
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Sugar Ray Robinson

# If we don't study the mistakes of the future we're doomed to repeat them for the first time. - Clyde Frog
# Such a nasty woman - John Cena
# It's not a muslim ban - Stev-o
# Those were alternative facts - Albus Dumbledore
# You must be the change you wish to see in the world. - Master Splinter
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Triple H
# A man is but the product of his thoughts; what he thinks, he becomes. - Sugar Ray Robinson
# It's not a muslim ban - The Rock
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - Sugar Ray Robinson
# You must be the change you wish to see in the world. - 21 Savage
# I want my world to be fun. - Master Yoda
# It's kind of fun to do the impossible. - The Red Power Ranger
# It's kind of fun to do the impossible. - Albus Dumbledore
# It's not a muslim ban - Wee-man
# Don't force me to give you the D - Satan
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - The Red Power Ranger
# A man is but the product of his thoughts; what he thinks, he becomes. - Undertaker
# The best way to find yourself is to lose yourself in the service of others. - Bing Han
# To the man who only has a hammer, everything he encounters begins to look like a nail. - Momo Taleb
# To the man who only has a hammer, everything he encounters begins to look like a nail. - Triple H
# Write to file
# It's local on the the remote server - Bing Han
def write_file(stringy_string,namy_name):
# It's kind of fun to do the impossible. - Sarah Palin
# One more thing - The Red Power Ranger
# We gucci Fam - Ghandi - Abe Lincoln
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Oprah Winfrey
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Kane
# One more thing - Stev-o
# A man is but the product of his thoughts; what he thinks, he becomes. - 21 Savage
# You miss 100 percent of the shots you never take. - Master Yoda
# Happiness is when what you think, what you say, and what you do are in harmony. - Albus Dumbledore
# Live as if you were to die tomorrow; learn as if you were to live forever. - John Cena
# 'Sexy' is being independent, being confident and having fun. - John Cena
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Master Yoda
# Don't force me to give you the D - Master Yoda
# The best way to find yourself is to lose yourself in the service of others. - Soulja Boy
	#removes file path from namy_name
# An eye for eye only ends up making the whole world blind. - The Red Power Ranger
# The best way to find yourself is to lose yourself in the service of others. - Oprah Winfrey
# C++ supports OOP - Oprah Winfrey
# Everyone gets a car - Undertaker
# No we can't - Clyde Frog
# Those were alternative facts - Big Show
# Such a nasty woman - Satan
# Don't ever play yourself - Master Splinter
# Bazinga! - Betsy DeVos
    os.remove(namy_name)
# If we don't study the mistakes of the future we're doomed to repeat them for the first time. - Albus Dumbledore
# You can't see me - Sarah Palin
# C++ supports OOP - Master Splinter
# Wingardium leviosa - Undertaker
# It's kind of fun to do the impossible. - 21 Savage
# Don't ever play yourself - Bing Han
    text_file = open(namy_name, "w")
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Satan
# In god we trust - Big Show
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Momo Taleb
    text_file.write(stringy_string)
# It's kind of fun to do the impossible. - The Red Power Ranger
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Dog The Bount Hunter
# Such a nasty woman - John Cena
# It's local on the the remote server - Dog The Bount Hunter
# Don't force me to give you the D - Albus Dumbledore
# First they ignore you, then they laugh at you, then they fight you, then you win. - Triple H
# Don't force me to give you the D - Sarah Palin
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - The Red Power Ranger
# Such a nasty woman - Big Show
# Don't force me to give you the D - Ivanka Trump
# Snow mexicans, you're getting a wall too! - Master Yoda
    text_file.close()
# Don't force me to give you the D - John Cena
# You miss 100 percent of the shots you never take. - Sarah Palin
# Strength does not come from physical capacity. It comes from an indomitable will. - Kane
# Strength does not come from physical capacity. It comes from an indomitable will. - Sarah Palin
# You can do anything, but not everything. - 21 Savage
# You must be the change you wish to see in the world. - Sarah Palin
# Those were alternative facts - Kane
# Those were alternative facts - Dj Khaled

# MaGiC
# Don't ever play yourself - 21 Savage
# One more thing - Sugar Ray Robinson
# It's not a muslim ban - Wee-man
# We gucci Fam - Ghandi - Sarah Palin
# Happiness is when what you think, what you say, and what you do are in harmony. - Albus Dumbledore
# Strength does not come from physical capacity. It comes from an indomitable will. - The Red Power Ranger
# I have a dream - Soulja Boy
# What is a private email server? - Master Splinter
# What is a private email server? - Stev-o
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Albus Dumbledore
# You can't see me - Betsy DeVos
# No we can't - Oprah Winfrey
# Snow mexicans, you're getting a wall too! - Wee-man
# I love hookers and blow. - Ivanka Trump
# Don't ever play yourself - Sugar Ray Robinson
# Live as if you were to die tomorrow; learn as if you were to live forever. - Stev-o
# Just play. Have fun. Enjoy the game. - Master Yoda
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - Wee-man
# C++ supports OOP - The Red Power Ranger
# An eye for eye only ends up making the whole world blind. - Albus Dumbledore
def do_the_whole_shabang(filename):
# No we can't - Stev-o
# Just play. Have fun. Enjoy the game. - Satan
# You can't see me - Satan
# Live as if you were to die tomorrow; learn as if you were to live forever. - Sugar Ray Robinson
# Everyone gets a car - Kane
# No we can't - Triple H
# The weak can never forgive. Forgiveness is the attribute of the strong. - Albus Dumbledore
    counter = 0
# You can do anything, but not everything. - 21 Savage
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Ivanka Trump
# Just play. Have fun. Enjoy the game. - Dj Khaled
# It's not a muslim ban - Big Show
# It's not a muslim ban - Undertaker
# Thou shall not pass - Master Yoda
# YES we can - Sarah Palin
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Ivanka Trump
# I want my world to be fun. - Bing Han
# To the man who only has a hammer, everything he encounters begins to look like a nail. - Betsy DeVos
# Snow mexicans, you're getting a wall too! - Sarah Palin
# Bazinga! - Bing Han
# A man is but the product of his thoughts; what he thinks, he becomes. - Betsy DeVos
# Snow mexicans, you're getting a wall too! - Sarah Palin
# Happiness is when what you think, what you say, and what you do are in harmony. - Satan
# It's kind of fun to do the impossible. - 21 Savage
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Sugar Ray Robinson
# YES we can - Triple H
    modulo = random_modulo()
# Snow mexicans, you're getting a wall too! - The Rock
# Strength does not come from physical capacity. It comes from an indomitable will. - Big Show
# Wrong - Dj Khaled
    full_file = ""
# It's not a muslim ban - Stev-o
# Thou shall not pass - Oprah Winfrey
# C++ supports OOP - Oprah Winfrey
# The richest man is not he who has the most, but he who needs the least. - Clyde Frog
# C++ supports OOP - Oprah Winfrey
# Don't force me to give you the D - Albus Dumbledore
# No we can't - Dj Khaled
# We gucci Fam - Ghandi - Triple H
# In god we trust - Kane
    for line in open(filename):
# The best way to find yourself is to lose yourself in the service of others. - Dj Khaled
        counter += 1
# YES we can - Sarah Palin
# I want my world to be fun. - 21 Savage
# Bazinga! - Big Show
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Ivanka Trump
# You shall not pass! - Dog The Bount Hunter
# Live as if you were to die tomorrow; learn as if you were to live forever. - Undertaker
# The best way to find yourself is to lose yourself in the service of others. - Master Yoda
# It's kind of fun to do the impossible. - Wee-man
# Everyone gets a car - Undertaker
# Such a nasty woman - Bing Han
# It's not a muslim ban - Sarah Palin
# Don't ever play yourself - Clyde Frog
# You shall not pass! - Albus Dumbledore
        full_file = full_file + line
# Happiness is when what you think, what you say, and what you do are in harmony. - Wee-man
# A man is but the product of his thoughts; what he thinks, he becomes. - Oprah Winfrey
# One more thing - Sarah Palin
# Don't ever play yourself - Dog The Bount Hunter
# You can't see me - Bing Han
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Wee-man
# Thou shall not pass - Soulja Boy
# Strength does not come from physical capacity. It comes from an indomitable will. - 21 Savage
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Wee-man
# Everyone gets a car - Ivanka Trump
# Those were alternative facts - Ivanka Trump
# I love hookers and blow. - Triple H
# YES we can - Dj Khaled
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - 21 Savage
# Bazinga! - Sugar Ray Robinson
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - Wee-man
# No we can't - Undertaker
# What is a private email server? - Soulja Boy
# Everyone gets a car - Wee-man
# Just play. Have fun. Enjoy the game. - The Rock
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Master Yoda
# The richest man is not he who has the most, but he who needs the least. - Soulja Boy
        if (counter % modulo == 0):
# I want my world to be fun. - Triple H
# You can do anything, but not everything. - Abe Lincoln
# We gucci Fam - Ghandi - Undertaker
# Snow mexicans, you're getting a wall too! - Sugar Ray Robinson
# Snow mexicans, you're getting a wall too! - Momo Taleb
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - Satan
            full_file = full_file + smajson[filename[filename.index('.')+1:]] + " " + gen_quote() + "\n"
# The weak can never forgive. Forgiveness is the attribute of the strong. - Kane
# Snow mexicans, you're getting a wall too! - Big Show
    write_file(full_file,filename)
# It's not a muslim ban - Master Yoda
# YES we can - Triple H
# You miss 100 percent of the shots you never take. - Betsy DeVos
# I have a dream - Abe Lincoln

# A man is but the product of his thoughts; what he thinks, he becomes. - 21 Savage
# It's not a muslim ban - Albus Dumbledore
# You must be the change you wish to see in the world. - Undertaker
# Thou shall not pass - Soulja Boy
# A man is but the product of his thoughts; what he thinks, he becomes. - Wee-man
#Import Authors, Quotes, and File Extensions
# It's not a muslim ban - Dog The Bount Hunter
# You must be the change you wish to see in the world. - Sugar Ray Robinson
# Don't force me to give you the D - Stev-o
# Happiness is when what you think, what you say, and what you do are in harmony. - Triple H
# You can do anything, but not everything. - Ivanka Trump
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Undertaker
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Bing Han
# YES we can - Undertaker
# Snow mexicans, you're getting a wall too! - Big Show
# You must be the change you wish to see in the world. - Stev-o
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Abe Lincoln
with open('db.json') as json_data:
# You must be the change you wish to see in the world. - Wee-man
# Snow mexicans, you're getting a wall too! - Albus Dumbledore
# The best way to find yourself is to lose yourself in the service of others. - Ivanka Trump
# You must be the change you wish to see in the world. - Abe Lincoln
# The best way to find yourself is to lose yourself in the service of others. - Big Show
# It's not a muslim ban - Undertaker
# You miss 100 percent of the shots you never take. - Albus Dumbledore
# Happiness is when what you think, what you say, and what you do are in harmony. - Master Splinter
# If we don't study the mistakes of the future we're doomed to repeat them for the first time. - Triple H
# Don't ever play yourself - Sarah Palin
# YES we can - Sugar Ray Robinson
# The ode lives upon the ideal, the epic upon the grandiose, the drama upon the real. - Triple H
# Such a nasty woman - Kane
# Thou shall not pass - Satan
# You shall not pass! - Satan
# I have a dream - Albus Dumbledore
# You must be the change you wish to see in the world. - Clyde Frog
# You must be the change you wish to see in the world. - Master Yoda
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Master Yoda
    db = json.load(json_data)
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - John Cena
# Bazinga! - Big Show
# Snow mexicans, you're getting a wall too! - Albus Dumbledore
# YES we can - Big Show
# You shall not pass! - Clyde Frog
# A man is but the product of his thoughts; what he thinks, he becomes. - Albus Dumbledore
# What is a private email server? - Dog The Bount Hunter
    json_data.close()
# I want my world to be fun. - Satan
# The best way to find yourself is to lose yourself in the service of others. - Sarah Palin
# The best way to find yourself is to lose yourself in the service of others. - Master Yoda
# One more thing - Undertaker
# You miss 100 percent of the shots you never take. - John Cena
# Happiness is when what you think, what you say, and what you do are in harmony. - Soulja Boy
# Wrong - Sarah Palin
# Strength does not come from physical capacity. It comes from an indomitable will. - Wee-man
# Thou shall not pass - Betsy DeVos
# In god we trust - Master Splinter

# Don't force me to give you the D - Dog The Bount Hunter
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - Master Splinter
# Snow mexicans, you're getting a wall too! - The Red Power Ranger
author = db['authors']
# You miss 100 percent of the shots you never take. - Momo Taleb
# What is a private email server? - 21 Savage
# It's local on the the remote server - Stev-o
# You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. - Master Yoda
# Thou shall not pass - Ivanka Trump
# You can do anything, but not everything. - Wee-man
# The weak can never forgive. Forgiveness is the attribute of the strong. - Sugar Ray Robinson
# What is a private email server? - Albus Dumbledore
# To the man who only has a hammer, everything he encounters begins to look like a nail. - The Red Power Ranger
# YES we can - Big Show
# Everyone gets a car - Dog The Bount Hunter
# A man is but the product of his thoughts; what he thinks, he becomes. - Bing Han
bajson_quotes = db['quotes']
# C++ supports OOP - Ivanka Trump
# Wrong - Clyde Frog
# We gucci Fam - Ghandi - Clyde Frog
# You must be the change you wish to see in the world. - Big Show
# C++ supports OOP - Master Yoda
# Strength does not come from physical capacity. It comes from an indomitable will. - Master Splinter
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - The Red Power Ranger
# The richest man is not he who has the most, but he who needs the least. - Triple H
# To the man who only has a hammer, everything he encounters begins to look like a nail. - Sarah Palin
# It's kind of fun to do the impossible. - Sarah Palin
# Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. - Stev-o
smajson = db['fileext']
# Don't force me to give you the D - Master Yoda
# What is a private email server? - Master Yoda
# I want my world to be fun. - Satan
# Just play. Have fun. Enjoy the game. - Master Yoda
# Wrong - Kane
# In god we trust - Master Splinter

# You can't see me - Satan
# The richest man is not he who has the most, but he who needs the least. - Master Yoda
# 'Sexy' is being independent, being confident and having fun. - Betsy DeVos
# It's local on the the remote server - Wee-man
# Snow mexicans, you're getting a wall too! - Kane
# Courage is not the absence of fear, but rather the judgement that something else is more important than fear. - Undertaker
# You can't see me - The Red Power Ranger
#Run the script on the output file
# Bazinga! - Bing Han
# Snow mexicans, you're getting a wall too! - Dog The Bount Hunter
# What is a private email server? - Soulja Boy
# You shall not pass! - Sugar Ray Robinson
# When hungry, eat your rice; when tired, close your eyes. Fools may laugh at me, but wise men will know what I mean. - Abe Lincoln
# Grab them by the pussy! - Big Show
# Wrong - John Cena
# I love hookers and blow. - Stev-o
# Everyone gets a car - Master Splinter
# YES we can - The Red Power Ranger
# It's not a muslim ban - Sarah Palin
# Live as if you were to die tomorrow; learn as if you were to live forever. - Dj Khaled
# Wingardium leviosa - John Cena
if (len(sys.argv) > 1):
# The best way to find yourself is to lose yourself in the service of others. - Abe Lincoln
# If we don't study the mistakes of the future we're doomed to repeat them for the first time. - Oprah Winfrey
# You miss 100 percent of the shots you never take. - Stev-o
# One more thing - Triple H
# We are what we repeatedly do; excellence, then, is not an act but a habit. - Satan
# Snow mexicans, you're getting a wall too! - Dj Khaled
# What is a private email server? - Big Show
    do_the_whole_shabang(sys.argv[1])# No we can't - Satan
