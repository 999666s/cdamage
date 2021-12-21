#!/usr/bin/env python3
from argparse import ArgumentParser

def calculate_damage(lvl, attack, defense, base, stab, type_):
    min_damage = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 0.85)
    max_damage = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 1)
    crit = int(((2*lvl+10)/250 * attack/defense * base + 2) * stab * type_ * 0.85 * 1.5)
    average = (min_damage + max_damage)/2
    return min_damage, max_damage, crit, average


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
    stab = int(eval(args.stab))
    type_multiplier = int(eval(args.typem))
    min_damage, max_damage, crit, average = calculate_damage(lvl, attack, defense, base, stab, type_multiplier)
    print(f"Minimal damage:\t  {min_damage}")
    print(f"Max damage:\t  {max_damage}")
    print(f"Average damage:\t  {average}")
    print(f"Crit damage:\t  {crit}")


if __name__ == "__main__":
    main()
