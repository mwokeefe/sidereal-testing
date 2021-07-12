#!/usr/bin/env python3

import pandas as pd
import ephem


def get_sidereal_time(date, obs):
    obs.date = date
    return str(obs.sidereal_time())


def main():
    # Open the csv file
    df = pd.read_csv('data.csv')

    # Convert DateTime from str to datetime
    df['DateTime'] = pd.to_datetime(df['DateTime'])

    # Initialise our observer
    obs = ephem.Observer()
    obs.lon = '+6.05528'
    obs.lat = '46.23556'

    # Calculate sidereal time in J2000 frame    
    df['J2000_ST'] = df['DateTime'].apply(get_sidereal_time, args=[obs])
    
    # Shift DateTime by 1895.6 hours
    delta = pd.Timedelta(hours=1895.6)
    df['DateTime'] -= delta

    # Now calculate sidereal time in SCF 
    df['SCF_ST'] = df['DateTime'].apply(get_sidereal_time, args=[obs])

    # Print our results
    print(df)


if __name__ == "__main__":
    main()
