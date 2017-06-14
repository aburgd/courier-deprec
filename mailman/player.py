from random import randint, choice


class PlayerCourier:

    """
    Defines a player Courier's base information
    SPECIAL - 7 basic stats
    Skills - affected by SPECIAL
    Traits - affect skills and SPECIAL
    """

    SPECIAL = {
        'strength': 5,
        'perception': 5,
        'endurance': 5,
        'charisma': 5,
        'intelligence': 5,
        'agility': 5,
        'luck': 5
    }

    SKILLS_LIST = ['energy weapons', 'melee weapons', 'guns', 'barter',
                   'repair', 'speech', 'explosives', 'unarmed', 'medicine']

    TRAITS_LIST = ['built to destroy', 'fast shot', 'four eyes',
                   'good natured', 'heavy handed',
                   'kamikaze', 'loose cannon', 'small frame',
                   'trigger discipline', 'wild wasteland']

    @classmethod
    def skill_tag(self):
        """
        Tags three skills from the list

        Returns:
            list
        """
        skills_list = PlayerMailman.SKILLS_LIST
        skills = ['', '', '']
        for item in skills:
            item_chosen = choice(skills_list)
            if item_chosen in skills:
                item_chosen = choice(skills_list)
                skills[skills.index(item)] = item_chosen
            else:
                skills[skills.index(item)] = item_chosen
        return skills

    @classmethod
    def traits_pick(self):
        """
        Picks two skills from the list

        Returns:
            list
        """
        traits_list = PlayerMailman.TRAITS_LIST
        traits = ['', '']
        for item in traits:
            item_chosen = choice(traits_list)
            if item_chosen in traits:
                item_chosen = choice(traits_list)
                traits[traits.index(item)] = item_chosen
            else:
                traits[traits.index(item)] = item_chosen
        return traits

    @classmethod
    def assign_attributes(self):
        """
        Assigns points to SPECIAL attributes at random

        Returns:
            dict
        """
        special = PlayerMailman.SPECIAL
        attributes = list(special.keys())
        for item in attributes:
            special[item] = randint(1, 10)
        return special
