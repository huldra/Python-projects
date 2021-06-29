import argparse
import requests
import csv
import retrieve_data
import datetime
import helper_functions
import input_verification
import sys

# ---------------------------- NOTES/ASSUMPTIONS--------------------------------"
"""
I Experimented a bit using the cbsodata module, but it seemed that the method get_data
returned the dataset on a different format than the TypedDataSet, so I decided to 
instead use the Requests library. The advantage with the cbsodata method was that I could 
read the data straight into a dictionary, but I did not find this easy to figure out
using requests.

I have been using regex before so I thought about that as an option.
Another advantage with using requests is that I could filter out the columns I was 
interested in the request. 
"""


def define_cmdline_options():
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--request_electricity', 
            action='store_true', default=False, 
            help='Option to retrieve electricity data')
    parser.add_argument('-n', '--request_natural_gas', 
            action='store_true', default=False, 
            help='Option to retrieve natural gas data')
    parser.add_argument('-sd', '--start_date', 
            type=str, default="1950-01-01", 
            help='start date to limit time range', metavar='yyyy-mm-dd')
    parser.add_argument('-ed', '--end_date', 
            type=str, default="2022-01-01", 
            help='end date to limit time range', metavar='yyyy-mm-dd')
    parser.add_argument('-f', '--frequency', 
            type=str, default='MM', 
            help='Frequency of value calculation, valid args: MM, KW or JJ', metavar='frequency')
    parser.add_argument('-fn', '--filename', 
            type=str, default='power_stats', 
            help='name of file to write collected data into, will be extended with commodity',
            metavar='filename')

    return parser

def request_data(cmdline_args):
    #if asked for, sending request to get electricity stats
    if cmdline_args.request_electricity:
        retrieve_data.get_electricity_stats(start_date, end_date,
                cmdline_args.frequency,
                cmdline_args.filename)
    
    #if asked for, sending request to get natural gas stats
    if cmdline_args.request_natural_gas:
        retrieve_data.get_gas_stats(start_date, end_date,
                cmdline_args.frequency,
                cmdline_args.filename)

    return


if __name__ == '__main__':

    #Define command line arguments
    cmdline_parser = define_cmdline_options()

    #Parse command line
    cmdline_args = cmdline_parser.parse_args()

    #Check if any request is given
    if cmdline_args.request_electricity == False and  cmdline_args.request_natural_gas == False:
        print("You have not requested any data to be retrieved, please type -h for help")
    
    #Verify input and convert dates
    input_verification.verify_input_frequency(cmdline_args)
    start_date, end_date = input_verification.verify_input_interval(cmdline_args)

    #Request data and write to file
    request_data(cmdline_args)


