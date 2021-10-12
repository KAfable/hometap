import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HOUSECANARY_API_KEY = os.getenv('HOUSECANARY_API_KEY')
HOUSECANARY_BASE_URL= os.getenv('HOUSECANARY_BASE_URL')

# constants
# note that https://api-docs.housecanary.com/#property-details has responses Pascal case strings, but actual mock data provided is snake case
RECOGNIZED_FALSE_RESPONSES = {
  'municipal',
  'storm',
  'septic',
  'none',
  'yes'
}
SEPTIC = 'septic'

def get_homecanary(address=None, zipcode=None):
  # temporary mock response until homecanary credentials
  if HOUSECANARY_BASE_URL == 'MOCK':
    with open('123-main-street.json') as json_file:
      response = json.load(json_file)

  # TODO: construct the query and make the call to the API and figure out where auth info goes
  if HOUSECANARY_API_KEY and HOUSECANARY_BASE_URL and HOUSECANARY_BASE_URL != 'MOCK':
    # always defaults to True for now
    return {
      'septic': True,
    }
  
  sewer = response['property/details']['result']['property']['sewer']
  
  if sewer == SEPTIC:
    result = True
    description = 'Verified'
  elif sewer in RECOGNIZED_FALSE_RESPONSES:
    result = False
    description = 'Verified'
  else:
    result = None
    description = 'Unknown'

  return {'result': result, 'description': description }
