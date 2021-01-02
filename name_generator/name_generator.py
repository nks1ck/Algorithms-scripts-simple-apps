"""infinite loop for getting random names"""
import sys
import random

# Pylint 9.44 / 10
def main():
    """Randomly select names from 2 tuples of names"""
    print("Hello, it's a funny name generator")

    first = ('Baby Oil', 'Bad News', 'Big Burps', 'Bill', 'Beenie-Weenie',
             'Bob Stinkbug', 'Bowel Noises', 'Boxelder', 'BudLite',
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
             'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet',
             'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
             'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
             'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
             'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
             'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
             'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
             'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff',
             'Scut’, "Sid The Squirts',
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
             'Soupcan Sam', 'Spitzitout’, ’Squids', 'Stinky', 'Storyboard',
             'Sweet Tea', 'TeeTee', 'Wheezy Joe', 'Winston' 'Jazz Hands', 'Worms')

    middle = ('Cox', 'Phfaer', 'Everret', 'Ivasishin', 'Boke')

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
        first_name = random.choice(first)

        last_name = random.choice(second)

        middle_name = random.choice(middle)

        print("\n\n")

        print("{} {} {}".format(first_name, middle_name, last_name), file=sys.stderr)

        try_again = input(
            "\n\nWill you try again? Enter for continue, N for exit\n")

        if try_again.lower() == "n":
            break


if __name__ == "__main__":
    main()
