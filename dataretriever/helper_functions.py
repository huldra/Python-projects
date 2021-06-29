import argparse
import requests
import csv
import datetime


def url_request(url,request_params):
    """Produce a response object from the given URL"""
    r = requests.request('GET',url,params=request_params)
    verify_request(r)
    return r


def verify_request(response):
    """Check if Client or server error is encountered"""
    if not response.ok:
        print("Client or server error")
        exit(0)


def create_data_point(line,frequency,commodity):
    """Convert line of data into dictionary"""
    if commodity == "el":
        data_point = {"Date" : convert_date_format(line[3],frequency), 
                "el-prod" : line[6].strip(":, "), "el-cons" : line[8].strip(":, ")}
    else:
        data_point = {"Date" : convert_date_format(line[3],frequency), 
                "gas" : line[6].strip(":, ")}
 
    return data_point


def write_data_point(data_point, linewriter, commodity, frequency, unit):
    """Write one data point on the right format to given filename"""
    line = [data_point['Date'], '00:00', data_point[commodity], commodity, frequency, unit]
    linewriter.writerow(line)


def get_data_from_line(line,frequency,commodity):
    """Clean up each line, and extract data of interest into a dict"""
    line = line.strip() #cleaning up
    line = line.split('"') #convert from string into list
    #extract data of interest into a dictionary
    data_point = create_data_point(line,frequency,commodity)
    return data_point


def convert_date_format(date_pattern,frequency):
    """Convert the format of the date from the form 1991MM02 to 1991-02-01"""
    year = int(date_pattern[:4])
    count = int(date_pattern[-2:])
    #Make it possible to choose any frequency
    if frequency == "KW":
        count = count*3 -2
    if frequency == "JJ":
        count = 1
    month = count
    new_format = datetime.datetime(year,month,1).date()
    #new_format = datetime.datetime.strptime(date_pattern, "%Y"+frequency+"%m").date() #BUG HERE
    return new_format


def is_in_time_range(curr_date,start_date,end_date):
    """Filters out data of interest from specified time period"""
    if curr_date >= start_date and curr_date <= end_date:
        return True
    return False


def format_frequency(frequency):
    """Convert to format expected in file"""
    options = {'MM':'monthly','KW':'Quarter wise','JJ':'yearly'}
    return options[frequency]
