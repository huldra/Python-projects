import argparse
import requests
import csv
from helper_functions import *


#TODO: Implement time range
#TODO: Remove duplicate code, more functions

def retrieve_electricity_stats(start_date,end_date,filename):
    """
    """
    #Select the columns we are interested in 
    electricity_params = {'$select':'Periods,GrossProduction_1,NetConsumptionCalculated_30'}
    #Found URL's navigating the cbs Data Portal in API (for Apps)
    url_electricity = "https://opendata.cbs.nl/ODataApi/odata/84575ENG/TypedDataSet"
    
    r = url_request(url_electricity,electricity_params)
    #TODO handle exeptions
    #print(r.url)
    with open(filename, 'w', newline='') as csvfile:
        linewriter = csv.writer(csvfile,delimiter=' ')
        for line in r.iter_lines(decode_unicode=True):
            if 'Periods' in line and 'MM' in line:
                #removing whitespace
                data_point = get_data_from_line(line)
                #print(data_point)
                write_data_point(data_point,linewriter,"el-prod","mlnkWh")
                write_data_point(data_point,linewriter,"el-cons","mlnkWh")


def retrieve_gas_stats(start_date,end_date):
    """
    

    """
    #Select the columns we are interested in 
    gas_params = {'$select':'Periods,GrossProduction_1'}
    #Found URL's navigating the cbs Data Portal in API (for Apps)
    url_gas = "https://opendata.cbs.nl/ODataApi/odata/00372eng/TypedDataSet"
    
    r = url_request(gas_params)

    #print(r.url)
    data_text = r.text.splitlines()
    #print(data_text)
    with open(filename, 'w', newline='') as csvfile:
        linewriter = csv.writer(csvfile)
        for line in data_text:
            txt = line.strip('{} ,')
            print(txt)
            write_data_line(txt,linewriter)
            #print(line.strip(''))

