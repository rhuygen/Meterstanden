import os, logging
import datetime
import numpy as np

HOME_DIR = os.path.expanduser('~')

def load_data():
    # Read the input csv file
    input_filename = 'Private/Git/Meterstanden/Data/Meterstanden.csv'
    
    logging.info("Reading input csv file from {}.".format(input_filename))

    data = np.recfromcsv(os.path.join(HOME_DIR, input_filename))
    
    # Convert the byte string b'' into a 'normal' string
    
    dt = np.array([datetime.datetime.strptime(x.decode('UTF-8'), '%Y-%m-%d %H:%M') for x in data['date_time']])

    return (data, dt)

