import gps
import os

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
menu = int(input("1. Print Latitude, Longitude, and Time\n2. Menu Screen\n"))
while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print("\n")
                if menu == 1:
                    print("Latitude:",report.lat)
                    print("Longitude:",report.lon)
                    print("Time:",report.time)
                if menu == 2:
                    os.system(r'cgps -s')
                if menu != 1 or 2:
                    print("It has to be either a 1 or a 2, reboot the script.")
                    quit()
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")