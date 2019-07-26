# -*- coding: utf-8 -*-
# /post_company.oy
import csv
import os
from gmaps import get_address


HURU_USER = os.environ.get('HURU_USER','factory@solidos.com')
HURU_USER_PASSWORD = os.environ.get('HURU_USER_PASSWORD','huru1234')
DEVICE = os.environ.get('DEVICE','29197302-98b2-f2a8-11a1-4030910140a0')
TARGET_URL = os.environ.get('TARGET_URL','http://localhost:8443')
ENDPOINT = os.environ.get('ENDPOINT','company')
FILE_PATH = os.environ.get('FILE_PATH','company.csv')
COMPANY_FIELDS = ['name', 'email', 'phone_region', 'phone_number', 'contact_name', 'contact_email', 'contact_phone_region', 
'contact_phone_number', 'website', 'description', 'address_coords', 'address_street', 'address_number', 'address_complement', 
'address_state', 'address_city', 'address_country', 'address_zip_code', 'date_created', 'updated_date', 'parent_id', 'type', 'cnpj', 'permissions']
ADDRESS_KEYS = ['name', 'address_country', 'address_state',  'address_city', 'address_street', 'address_number', 'address_complement', 'address_zip_code']


def make_post(arguments):
    return f"""curl -X POST -u {HURU_USER}:{HURU_USER_PASSWORD} -d "{arguments}" -H "X-NIC-DEVICE: {DEVICE}" {TARGET_URL}/{ENDPOINT}"""

def clean_data(raw_data):
    data = {}
    for key,value in raw_data.items():
        if value:
            key = key.lower()
            if key in COMPANY_FIELDS:
                if key == 'cnpj':
                    value = "".join([i for i in value if i.isdigit()])
                data[key] = value
    return data

def make_arguments(data):
    arguments = ''
    address = ""
    for key,value in data.items():
        arguments += f"{key}={value}&"
        if key in ADDRESS_KEYS:
            address += f"{value} "
    geodata = get_address({'address': address})
    if geodata:
        latitude, longitude = geodata['latitude'], geodata['longitude']
        arguments += f"latitude={latitude}&longitude={longitude}"
    return arguments[:-1] if arguments.endswith('&') else arguments

with open(FILE_PATH) as file:  
    data = csv.DictReader(file)
    for row in data:
        clean_row = clean_data(row)
        arguments = make_arguments(clean_row)
        post = make_post(arguments)
        os.system(post)

        
