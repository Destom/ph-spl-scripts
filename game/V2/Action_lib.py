import characters

def combat(oppnent):
    print(print_char_stats())


def print_char_stats():
    print("""your stats are
    Health {0} out of {1}
    attach {2}
    defence {3}
    evasion {4}""".format(str(characters.your_character.health),str(characters.your_character.max_health),str(characters.your_character.attack), str(characters.your_character.defence),str(characters.your_character.evasion)))
