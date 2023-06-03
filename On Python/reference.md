# Python Reference

## Contents
- [Current Time](#current-time)
- [Data Types](#data-types)
- [Dunder](#dunder)
- [Errors and Assert](#errors-and-assert)
- [Hello World](#hello_world)
- [Read and Write csv](#read-and-write-csv)
- [Read json](#read-json)
- [Read SQL](#read-sql)
- [Requirements File](#requirements-file)
- [S3](#s3)
- [String Manipulation](#string-manipulation)
- [Virtual Environments](#virtual-environments)

## Current Time

```python
import datetime
import time


if __name__ == '__main__':
    print(datetime.datetime.now())
    
    time.sleep(2.5)
    
    print(datetime.datetime.now())
```

## Data Types

```python
# Returns the data type
print(type('my_string'))

# Returns a boolean for data types
if isinstance('my_string', tuple):
    print('this is tuple')
```

## Dunder

```python
# Used to ensure code only runs if the script is run directly.
# Allows the script to be used as a module
if __name__ == '__main__':
    # Will only run if script is run directly
    print('hello world')
```

## Errors and Assert

```python
def my_function(my_number):
    return my_number

if __name__ == '__main__':
    try:
        assert my_function(1) == 1, 'Expected 1'
    except AssertionError as e:
        print(f'Test failed: {e}')
    except Exception as e:
        print(e)
    else:
        print('Test passed')
```

## Hello World

```python
# prints 'Hello World' to the terminal
print('Hello World')
```

## Read and Write csv

```python
import csv


if __name__ == '__main__':
    with open('input.csv', encoding='utf-8') as csvin:
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvout:
            spamreader = csv.reader(csvin)
            writer = csv.writer(csvout)
            for row in spamreader:
                # Do something
                print(row)
                writer.writerow(row)
```

## Read json

```python
import json


if __name__ == '__main__':
    with open('data.json', encoding='utf-8') as file:
        for line in file:
            #print(line)
            my_dict = json.loads(line)
            #print(my_dict[0]['key1'])
            print(my_dict[0].keys())
            for item in my_dict:
                print(item['key1'])
```

## Read SQL

```python
import psycopg2


if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="password"
    )
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM my_table LIMIT 10")
    print(f'rows returned {cur.rowcount}')
    row = cur.fetchone()

    while row is not None:
        print(row)
        print(row[0])
        row = cur.fetchone()

    cur.close()
```

## Requirements File

To create a requirements.txt used
```
pip freeze > requirements.txt
```

Packages can then be installed (to your venv) with 
```
pip install -r requirements.txt
```

## S3

Requires [AWS Boto3 Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) credentials.

```python
import boto3


if __name__ == '__main__':
    client = boto3.client('s3')
    
    response = client.list_buckets()
    
    for bucket in response['Buckets']:
        print(bucket['Name'])
```

## String Manipulation

```python
# define a string
my_string = 'the quick fox jumps over the lazy dog'

# prints my_string without the last three characters
print(my_string[:-3])

# prints my_string without the first four characters
print(my_string[4:])
```

## Virtual Environments

To create the virtual environment

```python
python -m venv my_venv
```

Enter the virtual environment in PowerShell with 

```
./my_venv/Scripts/Activate.ps1
```

You can now install packages to the virtual environment as normal. To exit the virtual environment 

```
deactivate
```

To the delete the virtual environment, you just need to delete the directory.