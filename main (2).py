#  implement a class player that represent a cricket player . the player class should have a method called daly which prints " the player is players cricket. derive two classes, batsman and bowler from the player class .override the play() method in each derived class to print "the batsman is batting and the bowler is bowling", respectively . write a program to create object of both batsman and bowler classes and call the play() method for each object in python"



# Define the base class player
class player :
   def play(self):
     print("The player is player cricket")

# define the derived class batsman 
class Batsman(player):
  def play(self):
    print("The batsman is batting")

# define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling")

# Create object of batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object 
batsman.play()
bowler.play()
