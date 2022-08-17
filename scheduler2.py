from datetime import datetime
from datetime import timedelta

get_appointment = datetime(2022, 5, 19, 6, 30)  # May 11, 2022 7:00 AM
travel_time = 3.5  # hours
preparation_time = 0.5  # hours
desired_sleep = 8  # hours

# get_appointment = str(input("Enter your appointment date and time (e.g. mm/dd/yyyy hh:mm): "))
# travel_time = input("Enter your travel time to the appointment in hours (e.g. 1, 1.5): ")
# preparation_time = input("Enter the amount of time needed to prepare for departure (e.g. 1, 1.5): ")
# desired_sleep = input("Enter the amount of sleep desired before starting your day (e.g. 1, 1.5): ")


class Schedule:
    def __init__(self, get_appointment, travel_time, preparation_time, desired_sleep):
        self.get_appointment = get_appointment
        self.travel_time = travel_time
        self.preparation_time = preparation_time
        self.desired_sleep = desired_sleep

    def departureTime(self):
        departure_time = get_appointment - timedelta(hours=travel_time)
        return departure_time

    def bedTime(self):
        departure_time = get_appointment - timedelta(hours=travel_time)
        bed_time = departure_time - timedelta(hours=preparation_time + desired_sleep)
        return bed_time

    def wakeUp(self):
        departure_time = get_appointment - timedelta(hours=travel_time)
        wake_up = departure_time - timedelta(hours=preparation_time)
        return wake_up


schedule = Schedule(get_appointment, travel_time, preparation_time, desired_sleep)

print(
    f"\nBed Time: {schedule.bedTime()}"
    f"\nWake Up: {schedule.wakeUp()}"
    f"\nDeparture Time: {schedule.departureTime()}"
)
