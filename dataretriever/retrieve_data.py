import argparse
import requests
import csv
from helper_functions import *


#TODO: Implement time range
#TODO: Remove duplicate code, more functions


def parse_and_write_el_data(response, frequency, start_date, end_date, linewriter):
    """
    Parse the lines of the response, filtering out the lines containing data
    If the date in inside our requested interval, the data is written to file.
    """
    commodity = "el"
    for line in response.iter_lines(decode_unicode=True):
        if 'Periods' in line and frequency in line:
            data_point = get_data_from_line(line,frequency,commodity)
            if is_in_time_range(data_point["Date"], start_date, end_date):
                print(data_point)
                write_data_point(data_point,linewriter,"el-prod",
                        format_frequency(frequency),"mlnkWh")
                write_data_point(data_point,linewriter,"el-cons",
                        format_frequency(frequency),"mlnkWh")
    return


def parse_and_write_gas_data(response, frequency, start_date, end_date, linewriter):
    """
    Parse the lines of the response, filtering out the lines containing data
    If the date in inside our requested interval, the data is written to file.
    """
    commodity = "gas"
    for line in response.iter_lines(decode_unicode=True):
        if 'Periods' in line and frequency in line:
            data_point = get_data_from_line(line,frequency,commodity)
            #print(data_point)
            if is_in_time_range(data_point["Date"], start_date, end_date):
                write_data_point(data_point,linewriter,"gas",
                        format_frequency(frequency),"mlnm3")
    return


def get_electricity_stats(start_date,end_date,frequency,filename):
    """
    """
    #Select the columns we are interested in 
    electricity_params = {'$select':'Periods,GrossProduction_1,NetConsumptionCalculated_30'}
    #Found URL's navigating the cbs Data Portal in API (for Apps)
    url_electricity = "https://opendata.cbs.nl/ODataApi/odata/84575ENG/TypedDataSet"
    
    r = url_request(url_electricity,electricity_params)
    #TODO handle exeptions
    filename = filename+"_electricity.csv"

    with open(filename, 'w', newline='') as csvfile:
        linewriter = csv.writer(csvfile,delimiter=' ')
        parse_and_write_el_data(r, frequency, start_date, end_date, linewriter)


def get_gas_stats(start_date,end_date,frequency,filename):
    """
    

    """
    #Select the columns we are interested in 
    gas_params = {'$select':'Periods,ElectricityPowerPlants_12'}
    #Found URL's navigating the cbs Data Portal in API (for Apps)
    url_gas = "https://opendata.cbs.nl/ODataApi/odata/00372eng/TypedDataSet"

    r = url_request(url_gas,gas_params)
    filename = filename+"_natural_gas.csv"

    with open(filename, 'w', newline='') as csvfile:
        linewriter = csv.writer(csvfile,delimiter=' ')
        parse_and_write_gas_data(r, frequency, start_date, end_date, linewriter)



