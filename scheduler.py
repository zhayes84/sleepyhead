from datetime import datetime
from datetime import timedelta

apptTime = datetime(2022, 5, 11, 7, 00) # May 11, 2022 7:00 AM
travelTime = 3 # hours, but will need to accept minutes eventually

departureTime = apptTime - timedelta(hours=travelTime)
prepTime = 30 # minutes

desiredSleep = 9 # hours
wake_up = departureTime - timedelta(hours=prepTime / 60)
bed_time = departureTime - timedelta(hours=(prepTime / 60) + desiredSleep)

print(
    f"\nBed Time: {bed_time}"
    f"\nWake Up: {wake_up}"
    f"\nDeparture Time: {departureTime}"
)