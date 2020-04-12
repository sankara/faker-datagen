# faker-datagen
A jok2k/faker based docker image to generate data based on a given schema

### From CLI:
```
usage: generator.py [-h] -s SCHEMA [-f OUTPUT_FILE] [-n COUNT] [-t FREQUENCY]

optional arguments:
  -h, --help            show this help message and exit
  -s SCHEMA, --schema SCHEMA
                        (env=FAKER_SCHEMA) JSON string representing the schema in a simple <name>:<datatype> format
  -f OUTPUT_FILE, --output-file OUTPUT_FILE
                        (env=FAKER_FILE) A file name to write the data out. (CSV). Uses stdout if not specified
  -n COUNT, --count COUNT
                        (env=FAKER_COUNT) The number of rows to generate per call
  -t FREQUENCY, --frequency FREQUENCY
                        (env=FAKER_FREQ) This enables generating continuously at the given frequency (per second)
```

### From Docker:
Refer [./docker-compose.yml](./docker-compose.yml)
