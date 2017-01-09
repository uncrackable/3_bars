import json
import math

def load_data(filepath):
    with open(filepath,'r',encoding='cp1251') as json_to_parse:
        json_to_parse = json.loads(json_to_parse.read())
    return json_to_parse


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar

def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    filepath = input('Enter file path: ')
    json_content = load_data(filepath)
    print ('Biggest bar is ', get_biggest_bar(json_content)['Name'], ':', get_biggest_bar(json_content)['SeatsCount'])
    print ('Smallest bar is ', get_smallest_bar(json_content)['Name'], ':', get_smallest_bar(json_content)['SeatsCount'])