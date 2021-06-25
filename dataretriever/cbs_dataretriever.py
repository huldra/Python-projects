import argparse



# Command Line Options --------- #
parser = argparse.ArgumentParser()

parser.add_argument('-e', '--electricity', action='store_true', default=False, help='Option to retrieve electricity data')
parser.add_argument('-n', '--natural', action='store_true', default=False, help='Option to retrieve natural gas data')
parser.add_argument('-sd', '--start_date', type=str, default=None, help='start date to limit time range', metavar='start_date')
parser.add_argument('-ed', '--end_date', type=str, default=None, help='end date to limit time range', metavar='end_date')


args = parser.parse_args()
electricity = args.electricity
natural_gas = args.natural
t0 = args.start_date
t1 = args.end_date
# ------------------------------ #


#TODO: CHECK THAT END DATE IS AFTER START DATE
#TODO: HANDLE CASE IF ARGUMENTS ARE NOT VALID


