#! /usr/bin/python3

import argparse
from hashlib import new
import typing
import json
import pprint


PIZZA_PERCENTAGES = {
    "flour": 100,
    "water": 67,
    "salt": 2,
    "starter": 15,
}


def bakers_percentage_calc(desired_weight: int, optional_ingredient=None) -> dict:
    """
    bakers_percentage_calc takes a given weight, and uses either a
    defined dict of ingredient percentages (with the option to add optional ingredients),
    calculates the new total, and returns in dict / json form the final result

    :desired weight: total dough yield desired
    :optional_ingredient: optional ingredients in form of key value pairs, ie malt=2 (the number resembles a percentage)
    :return: json object of final result
    """
    new_totals = {}

    # Get sum of all ingredient percentages
    percent_sum = float(sum(list(PIZZA_PERCENTAGES.values())))

    # Get the percentage of ingredients: formula desired weight amount / sum of base percentages
    ingredient_percent = float(f"{float(desired_weight/percent_sum):.2f}")

    new_totals = {
        "flour": ingredient_percent * PIZZA_PERCENTAGES["flour"],
        "water": ingredient_percent * PIZZA_PERCENTAGES["water"],
        "salt": ingredient_percent * PIZZA_PERCENTAGES["salt"],
        "starter": ingredient_percent * PIZZA_PERCENTAGES["starter"],
    }

    if optional_ingredient:
        for ingredient in optional_ingredient:
            optional_ingredient[ingredient] = float(optional_ingredient[ingredient])
            optional_ingredient[ingredient] = f"{float(optional_ingredient[ingredient] * ingredient_percent):.2f}"
            new_totals.update(optional_ingredient)

    return new_totals


def parser():
    parser = argparse.ArgumentParser(description='Simple Bakers Calculator for Sourdough')
    parser.add_argument('-w','--weight', help='Desired dough yield', required=True, type=float)
    parser.add_argument('-o', '--optional-ingredient', action=ParseKwargs, nargs='*')
    args = vars(parser.parse_args())

    return args


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value


def main():

    arg_parser = parser()

    weight = arg_parser["weight"]
    optional_ingredients = arg_parser["optional_ingredient"] if arg_parser["optional_ingredient"] else None
    output = bakers_percentage_calc(weight, optional_ingredients=optional_ingredients)
    pprint.pprint(output)
    

if __name__ == '__main__':

    main()
