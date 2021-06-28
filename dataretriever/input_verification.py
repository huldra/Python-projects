import datetime

    
def verify_input_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Given date is not valid, please use the following format: yyyy-mm-dd")
        sys.exit(0)
    return date

def verify_input_frequency(args):
    if args.frequency in ['MM','KW','YY']:
        continue
    else:
        print("Invalid value for frequency, please specify either MM, KW or YY")
        sys.exit(0)
    return True  

def verify_input_interval(args):
    """ Check that end date is after start date"""
    if verify_input_date(args.end_date) > verify_input_date(args.start_date)
        return True
    else:
        raise ValueError ("Start date is after end date, not a valid time interval"
