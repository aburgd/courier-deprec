from player import PlayerCourier
from util import roll_check


mojave = PlayerCourier()
name_gender = mojave.name_gender()
mojave_name = mojave.tell_me_your_name(name_gender)
mojave_gender = mojave.display_gender()
mojave_special = mojave.assign_attributes()
mojave_special = roll_check(mojave_special)
mojave_skills = mojave.skill_tag()
mojave_traits = mojave.traits_pick()

print("Name: {}".format(mojave_name))
print("Gender: {}".format(mojave_gender))
print("SPECIAL: {}".format(mojave_special))
print("Skills: {}".format(mojave_skills))
print("Traits: {}".format(mojave_traits))
