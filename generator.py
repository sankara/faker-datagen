from faker import Faker
import os
import argparse
import json
import csv
import sys
import time
import signal
from threading import Event

#List of support datatypes: https://faker.readthedocs.io/en/stable/providers.html
#In addition: https://faker.readthedocs.io/en/stable/providers/faker.providers.misc.html
def generate_data(schema, count=1):
    data = []
    f = Faker()
    for i in range(count):
        data.append({})
        for k,v in schema.items():
            val = f.format(v)
            if isinstance(val, str):
                val = val.replace('\n', '|').replace('\r', '')
            data[i][k] = val
    return data

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--schema", help="(env=FAKER_SCHEMA) JSON string representing the schema in a simple <name>:<datatype> format")
    parser.add_argument("-f", "--output-file", help="(env=FAKER_FILE) A file name to write the data out. (CSV). Uses stdout if not specified")
    parser.add_argument("-n", "--count", type=int, help="(env=FAKER_COUNT) The number of rows to generate per call")
    parser.add_argument("-t", "--frequency", type=float, help="(env=FAKER_FREQ) This enables generating continuously at the given frequency (per second)")

    return parser.parse_args()

def write_to_csv(data, out):
    w = csv.DictWriter(out, fieldnames = data[0].keys())
    for r in data:
        w.writerow(r)

def with_open_file_or_stdout(filename, l):
    if filename:
        with open(filename, 'a', newline='') as out:
            l(out)
    else:
        l(sys.stdout)

exit = Event()

def main():
    args = get_args()
    schema_s = os.environ['FAKER_SCHEMA'] if 'FAKER_SCHEMA' in os.environ else args.schema
    filename = os.environ['FAKER_FILE'] if 'FAKER_FILE' in os.environ else args.output_file
    freq_per_s = float(os.environ['FAKER_FREQ']) if 'FAKER_FREQ' in os.environ else args.frequency
    count = int(os.environ['FAKER_COUNT']) if 'FAKER_COUNT' in os.environ else args.count
    if not count:
        count = 1

    #if count is given, generate count rows and write to file/out
    #else loop infinite, generate a row, write to file, sleep


    schema = json.loads(schema_s)

    with_open_file_or_stdout(filename, lambda out: csv.DictWriter(out, fieldnames = schema.keys()).writeheader())

    while not exit.is_set():
        data = generate_data(schema, count)
        with_open_file_or_stdout(filename, lambda out: write_to_csv(data, out))
        if not freq_per_s:
            break
        time.sleep(1/freq_per_s)


if __name__ == "__main__":
    for sig in [signal.SIGTERM, signal.SIGHUP, signal.SIGINT]:
        signal.signal(sig, (lambda x,y: exit.set()))
    main()
