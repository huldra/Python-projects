import argparse
import requests
import csv
import retrieve_data

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

    parser.add_argument('-e', '--electricity_option', 
            action='store_true', default=False, 
            help='Option to retrieve electricity data')
    parser.add_argument('-n', '--natural_gas_option', 
            action='store_true', default=False, 
            help='Option to retrieve natural gas data')
    parser.add_argument('-sd', '--start_date', 
            type=str, default=None, 
            help='start date to limit time range', metavar='start_date')
    parser.add_argument('-ed', '--end_date', 
            type=str, default=None, 
            help='end date to limit time range', metavar='end_date')
    parser.add_argument('-fn', '--filename', 
            type=str, default='power_stats.csv', 
            help='name of file to write collected data into', metavar='filename')

    return parser.parse_args()





def main(electricity, natural_gas):
    if electricity:
        retrieve_electricity_stats(t0,t1)
    if natural_gas:
        retrieve_gas_stats(t0,t1)


#TODO: CHECK THAT END DATE IS AFTER START DATE
#TODO: HANDLE CASE IF ARGUMENTS ARE NOT VALID

if __name__ == '__main__':
    cmdline_parser = define_cmdline_options()
    print(cmdline_parser.electricity_option)
    print(retrieve_data.convert_date_format("2018MM02"))
    #parse command line()
    #sender forespørsel til url dersom dette ønskes()
    #sjekker om ok()
    #henter data ut i streng()
    retrieve_data.retrieve_electricity_stats(0,1,cmdline_parser.filename)
