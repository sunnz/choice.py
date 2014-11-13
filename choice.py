#!/usr/bin/env python3

import sys
import yaml
import random


def main():
    if len(sys.argv) < 2:
        print('Using meals.yaml. You can pass your own meals.yaml file as '
              'the first argument on the command line too.')
        print()
        print('For example: ' + sys.argv[0] + ' meals.yaml')
        print()
        meals_config = 'meals.yaml'
    else:
        meals_config = sys.argv[1]

    meals = []
    try:
        with open(meals_config, 'r') as f:
            meals = yaml.load(f)
    except (OSError, IOError) as e:
        print('Cannot open file ' + meals_config + '. :-(')
        sys.exit(1)

    if not meals:
        print('No meals loaded. :-(')
        sys.exit(1)

    ans = ''
    while 'no' != ans.lower():
        print(random.choice(meals))
        ans = input('continue? (yes/no) [yes] ')

if __name__ == '__main__':
    main()
