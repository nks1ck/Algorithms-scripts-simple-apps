import sys
import random

# Pylint 7.14/10
print("Hello, it's a funny name generator")


first =  ('Baby Oil', 'Bad News', 'Big Burps', 'Bill', 'Beenie-Weenie',
          'Bob Stinkbug', 'Bowel Noises', 'Boxelder', 'BudLite' ,
          'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
          'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet',
          'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
          'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
          'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
          'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
          'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
          'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
          'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
          'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo','Scratchensniff', 
          'Scut’, "Sid The Squirts',
          'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
          'Soupcan Sam', 'Spitzitout’, ’Squids', 'Stinky', 'Storyboard',
          'Sweet Tea', 'TeeTee', 'Wheezy Joe', 'Winston' 'Jazz Hands','Worms')

second = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
          'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
          'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
          'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
          'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
          'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
          "MBernbo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
          'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
          'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
          'Porkins', 'Putney', 'Quakenbush’, ’Rainwater', 'Rosenthal',
          'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
          'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
          'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
          'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
          'Winterkorn', 'Woolysocks')


while True:
    """infinite loop for getting random names"""
    firstName = random.choice(first)

    lastName = random.choice(second)

    print("\n\n")

    print("{} {}".format(firstName, lastName), file=sys.stderr)

    try_again = input("\n\nWill you try again? Enter for continue, N for exit\n")

    if try_again.lower() == "n":
        break
