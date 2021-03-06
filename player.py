# Player Class
#   Manages the powers and abilities of the player

__author__="rosbaldeston"
__date__ ="$Jan 9, 2012 10:14:59 AM$"

import attributes

class player:
	# Class controls the player information
	def __init__(self, startingClass):
		self.player = attributes.Attributes(startingClass)
		
	def skills(self):
		return self.player.skills.activated()

	def powers(self):
		return self.player.powers.activated()

	def computeDamageOutput(self, attack, associatedPerks):
		None

	def computeDamageInput(self, attack, associatedPerks):
		None

	def getDefenseRating(self, against):
		return (self.defense / (self.defense + against))
	
	def printClassStats(self):
		print "\n\nYou have chosen to be a " + startingClass + "!"
		print "Hit Points: ", User.player.getHP()
		print "Stamina Points: ", User.player.getStamina()
		print "Vitavis Points: ", User.player.getVP()
		print "Madness Points: ", User.player.getMP()
		print "Base Power Damage: ", User.player.getBasePowerDamage()
		print "Base Dex Damage: ", User.player.getBaseDexSkillDamage()
		print "Base Str Damage: ", User.player.getBaseStrSkillDamage()
		print "Def Vs Physical: ", User.player.getBaseDefenseVsPhysical()
		print "Def Vs Magic: ", User.player.getBaseDefenseVsMagic()
		print "Dodge Likelihood: ", User.player.getDodgeLikelihood()
		print "Critical Hit Chance: ", User.player.getCriticalHitChance()

	def subPrimeDefinitions(self):
		print "\n\nA sub-prime is a secondary skill or power in which your class is also proficient."
		print "You may choose two sup-primes from the lists below"
		print "Skills: [Archery, One-Handed, Shield, Staff, Two-Handed, Unarmed]"
		print "Powers: [Blink, Fire, Hydras, Light, Manipulation, Mend, Sense, Shift, Sight, Step, Strength, Terra]"
		subPrimeOne = raw_input("What would you like your first sub-prime to be? ")
		subPrimeTwo = raw_input("What would you like your second sub-prime to be? ")
		self.player.createSubPrimes(subPrimeOne, subPrimeTwo)

	def spendInitialPerks(self):
		print "\n\nYou may start with three perks. \nThese perks can be spent and any of the 18 ability trees."
		print "Though it is suggested that they are used in the primary trees associated with your"
		print "chosen class or one of the two sub primes."

if __name__ == "__main__":
	print "Welcome!"
	print "You may choose from the following list of classes for your starting class."
	print "[Wytch, Thief, Warrior, Mage, Descendent, Assassin, Healer, Seer, Ranger, Wanderer]"
	startingClass = raw_input("What Class would you like to be? ")
	User = player(startingClass)
	User.printClassStats()
	User.subPrimeDefinitions()
