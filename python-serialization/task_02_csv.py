#!/usr/bin/env python3
import json
import csv


def convert_csv_to_json(filename):
    """takes the CSV filename as its parameter and writes
    the JSON data"""
    try:
        data_list = []

        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)
        return True
    except Exception:
        return False
