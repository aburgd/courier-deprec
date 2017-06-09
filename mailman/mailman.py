from player import PlayerMailman


mojave = PlayerMailman()
mojave_special = mojave.assign_attributes()
mojave_skills = mojave.skill_tag()
mojave_traits = mojave.traits_pick()

print("Your Courier\n")
print("SPECIAL: {}".format(mojave_special))
print("Skills: {}".format(mojave_skills))
print("Traits: {}".format(mojave_traits))
