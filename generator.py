from faker import Faker
import os
import argparse
import json
import csv
import sys

#List of support datatypes: https://faker.readthedocs.io/en/stable/providers.html
#In addition: https://faker.readthedocs.io/en/stable/providers/faker.providers.misc.html
def generate_row(schema):
    data = {}
    f = Faker()
    for k,v in schema.items():
        data[k] = f.format(v)
    return data

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--schema", help="JSON string representing the schema in a simple <name>:<datatype> format")
    parser.add_argument("-f", "--output-file", help="A file name to write the data out. (CSV). Uses stdout if not specified")

    return parser.parse_args()

def write_to_csv(data, out):
    w = csv.DictWriter(out, fieldnames = data[0].keys())
    w.writeheader()
    for r in data:
        w.writerow(r)

def main():
    args = get_args()
    schema_s = os.environ['FAKER_SCHEMA'] if 'FAKER_SCHEMA' in os.environ else args.schema
    file_name = os.environ['FAKER_FILE'] if 'FAKER_FILE' in os.environ else args.output_file

    schema = json.loads(schema_s)
    data = [generate_row(schema)]

    if file_name:
        with open(file_name, 'w') as csv_file:
            write_to_csv(data, csv_file)
    else:
        write_to_csv(data, sys.stdout)

if __name__ == "__main__":
    main()
