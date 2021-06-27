import argparse
import requests
import csv

def url_request(url,request_params):
    """Produce a response object from the given URL"""
    r = requests.request('GET',url,params=request_params)
    request_verification(r)
    return r

def request_verification(response):
    """Check if Client or server error is encountered"""
    if not response.ok:
        print("Client or server error")
        exit(0)

def create_data_point(line):
    data_point = {"Date" : convert_date_format(line[3]), 
            "el-prod" : line[6].strip(":, "), "el-cons" : line[8].strip(":, ")}
    return data_point

def get_data_from_line(line):
    line = line.strip() #cleaning up
    line = line.split('"') #convert from string into list
    #extract data of interest into a dictionary
    data_point = create_data_point(line)
    return data_point

def convert_date_format(date_pattern):
    """Converts the format of the date from ex. 1991MM02 to 1991.02.01"""
    new_format = ""
    new_format += date_pattern[:4]+"-"+date_pattern[-2:]+"-01"
    return new_format

def write_data_point(data_point, linewriter, commodity, unit):
    """Write one line of the data file with the right format to given filename"""
    line = [data_point['Date'], '00:00', data_point[commodity], commodity, 'monthly', unit]
    linewriter.writerow(line)
    
