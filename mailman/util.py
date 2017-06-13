from player import PlayerMailman


def roll_check(special):
    """
    Checks if a rolled SPECIAL is valid. Returns the argument if it is,
    rerolls if it isn't.

    Returns:
        dict
    """
    valid = special_validation(special)
    if valid is True:
        return special
    if valid is False:
        special = rerolling(valid, special)
        roll_check(special)
        return special


def rerolling(valid, player_special):
    """
    Double-checks roll_check for validity of SPECIAL.

    Returns:
        dict
    """
    if valid is True:
        return player_special
    elif valid is False:
        player = PlayerMailman()
        player_special = player.assign_attributes()
        return player_special


def special_validation(player_special):
    """
    Takes a dict of attributes and returns a boolean based
    on the sum of the attributes' keys.

    Returns:
        bool
    """
    attributes = list(player_special.keys())
    attr_sum = 0
    for item in attributes:
        attr_sum += player_special[item]
    if attr_sum > 40 or attr_sum < 40:
        return False
    elif attr_sum == 40:
        return True
