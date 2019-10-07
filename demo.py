#! /usr/bin/python

import sys
import glob
import json
import statistics

# Directory & file names
DIRECTORY = 'data/'
FILE = '*'
SEPARATOR = '.'
EXTENSION = 'json'

# CLI parameters
AVG = '--avg'
MAX = '--max'
MEDIAN = '--median'
MIN = '--min'

# Error codes
ERR_ILLEGAL_TYPE = 100
ERR_USAGE = 101
ERR_DATA_FILE = 102
ERR_EMPTY_LIST = 103

def usage():
  print('Usage: ./demo.py <--avg | --max | --median | --min>')
  sys.exit(ERR_USAGE)

def load(file_name):
  output = None

  try:
    fh = open(file_name, "r")
    return json.load(fh)

    fh.close()
  except IOError:
    print('Data file not loaded.')
    sys.exit(ERR_DATA_FILE)

def extract():
  files = glob.glob(DIRECTORY + FILE + SEPARATOR + EXTENSION)
  data = []
  types = []

  for f in files:
    tmp_records = load(f).values()
    
    for tr in tmp_records:
      i = 0

      while i < len(tr):
        rd = {}

        try:
          types.append(tr[i]['type'])
          rd['type'] = tr[i]['type']
          rd['amount'] = tr[i]['amount']
          data.append(rd)

          i += 1
        except IndexError:
          break

  return data, types

def calculate(purchases, command, purchase_type):
  amounts = []
  output = None

  for p in purchases:
    if p['type'] == purchase_type:
      amounts.append(int(p['amount']))

  if len(amounts) > 0:
    if command == AVG:
      output = 'AVG = ' + str(statistics.mean(amounts))
    elif command == MEDIAN:
      output = 'MEDIAN = ' + str(statistics.median(amounts))
    elif command == MAX:
      output = 'MAX = ' + str(max(amounts))
    elif command == MIN:
      output = 'MIN = ' + str(min(amounts))
    else:
      usage()

    return purchase_type + ': ' + output + ', COUNT = ' + str(len(amounts))
  else:
    print('Empty amount list.')
    sys.exit(ERR_EMPTY_LIST)

if __name__ == '__main__':
  try:
    if len(sys.argv) >= 2:
      command = sys.argv[1]
      purchase_type = sys.argv[2]

      purchases = extract()

      if purchase_type in purchases[1]:
        print(calculate(purchases[0], command, purchase_type))
      else:
        print('Purchase type ' + purchase_type + ' NOT among registered ones.')
        sys.exit(ERR_ILLEGAL_TYPE)
  except IndexError:
    usage()
