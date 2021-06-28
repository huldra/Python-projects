import datetime
import sys

    
def verify_input_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Given date is not valid, please use the following format: yyyy-mm-dd")
        sys.exit(0)
    return date

def verify_input_frequency(args):
    if args.frequency not in ['MM','KW','JJ']:
        print("Invalid value for frequency, please specify either MM, KW or JJ")
        sys.exit(0)
    return True  

def verify_input_interval(args):
    """ Check that end date is after start date"""
    t0 = verify_input_date(args.start_date)
    t1 = verify_input_date(args.end_date)
    if t0 > t1:
        raise ValueError ("Start date is after end date, not a valid time interval")
    return (t0,t1)

