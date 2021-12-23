#!/usr/bin/env python3
from argparse import ArgumentParser

def calculate_damage(lvl, attack, defense, base, stab, type_):
    min_damage = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 0.85)
    max_damage = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 1)
    crit_min = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 0.85 * 1.5)
    crit_max = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 1 * 1.5)
    average = (min_damage + max_damage)/2
    return min_damage, max_damage, crit_min, crit_max, average


def main():
    parser = ArgumentParser()
    parser.add_argument("lvl", type=str, help="Lead pokemon lvl")
    parser.add_argument("attack", type=str, help="Lead pokemon attack")
    parser.add_argument("defense", type=str, help="Defensive pokemon defense")
    parser.add_argument("base", type=str, help="Attack base")
    parser.add_argument("stab", type=str, help="Stab multiplier")
    parser.add_argument("typem", type=str, help="Type multiplier")
    args = parser.parse_args()

    lvl = int(eval(args.lvl))
    attack = int(eval(args.attack))
    defense = int(eval(args.defense))
    base = int(eval(args.base))
    stab = float(eval(args.stab))
    type_multiplier = float(eval(args.typem))
    min_damage, max_damage, crit_min, crit_max, average = calculate_damage(lvl, attack, defense, base, stab, type_multiplier)
    #print(f"{lvl=} {attack=} {defense=} {base=} {stab=} {type_multiplier=}")
    print(f"Damage:\t{min_damage}-{max_damage} Avrg: {average} Crit: {crit_min}-{crit_max}")


if __name__ == "__main__":
    main()
