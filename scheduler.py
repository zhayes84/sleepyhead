from datetime import datetime, timedelta
import time

start_time = time.time()


class Day:
    """
    A Day object consists of all necessary information needed to
    compute a schedule or all days of the week.

    'have_work': boolean determining whether user has work on this specified day

    'work_time': datetime object specifying year/month/day/hour/minute

    'commute': time required to drive from home to work

    'departure': the time required to leave home to make it to work by 'work_time'

    'prep' is how much time is needed to prepare for work after waking up

    'time_in_bed': desired number of hours in bed

    'bed_time': time to go to bed based on 'work_time' minus 'prep' minus 'time in bed'

    'wake_up': time to wake up
    """

    def __init__(self, have_work, work_time, commute, prep, time_in_bed):
        self.have_work = have_work
        self.work_time = work_time
        self.commute = commute
        self.prep = prep
        self.time_in_bed = time_in_bed

    def departure(self):
        """
        Takes the time to be at work subtracted by the commute time and
        returns the necessary departure time to arrive at work on time.
        """
        commute_object = timedelta(minutes=self.commute)
        work_time_object = datetime.strptime(self.work_time, "%B %d, %Y %I:%M %p")
        return work_time_object - commute_object

    def bed_time(self):
        prep_object = timedelta(hours=self.prep)
        time_in_bed_object = timedelta(hours=self.time_in_bed)
        commute_object = timedelta(minutes=self.commute)
        work_time_object = datetime.strptime(self.work_time, "%B %d, %Y %I:%M %p")
        return datetime.strftime(
            ((work_time_object - commute_object) - (prep_object + time_in_bed_object)),
            "%B %d, %Y %I:%M %p",
        )  # displays bed_time in 'MMMM DD, YYYY T:TT AM' format

    def wake_up(self):
        commute_object = timedelta(minutes=self.commute)
        work_time_object = datetime.strptime(self.work_time, "%B %d, %Y %I:%M %p")
        prep_object = timedelta(hours=self.prep)
        return datetime.strftime(
            ((work_time_object - commute_object) - prep_object), "%B %d, %Y %I:%M %p"
        )


thursday = Day(True, "August 17, 2022 2:00 AM", 30, 1, 8)

print(
    f"\ntime_in_bed = {thursday.time_in_bed}"
    f"\nhave_work = {thursday.have_work}"
    f"\nwork_time = {thursday.work_time}"
    f"\ncommute = {thursday.commute} minutes"
    f"\nbed time = {thursday.bed_time()}"
    f"\nwake up = {thursday.wake_up()}"
    f"\nprep time = {thursday.prep} hour"
    f"\ndeparture = {thursday.departure()}"
)

print(f"\nProcess finished in {time.time() - start_time} seconds")
