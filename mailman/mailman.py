from player import PlayerMailman
from util import roll_check


mojave = PlayerMailman()
mojave_special = mojave.assign_attributes()
mojave_special = roll_check(mojave_special)
mojave_skills = mojave.skill_tag()
mojave_traits = mojave.traits_pick()

print("Your Courier")
print("SPECIAL: {}".format(mojave_special))
print("Skills: {}".format(mojave_skills))
print("Traits: {}".format(mojave_traits))
