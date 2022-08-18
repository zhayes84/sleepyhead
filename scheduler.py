from datetime import datetime, timedelta
import time


class Day:
    """The Day class consists of all necessary information needed to
    compute a schedule for all days of the week.

    Attributes
    ----------

    have_work : bool
        boolean determining whether user has work on this specified day

    work_time : str
        datetime object specifying year/month/day/hour/minute

    commute : int
        time required to drive from home to work

    prep : int
        how much time is needed to prepare for work after waking up

    time_in_bed : int
        desired number of hours in bed

    Methods
    -------

    departure()
        Returns datetime object containing the time of departure.

    bed_time()
        Returns datetime object containing the time to go to bed.

    wake_up()
        Returns datetime object containing the time to wake up.
    """

    def __init__(self, have_work, work_time, commute, prep, time_in_bed):
        """Constructs all the necessary attributes for the Day object.

        Args:
            have_work (bool): whether the user has work on the day
            work_time (str): time to arrive at work
            commute (int): time required to drive from home to work
            prep (int): time required to prepare for work after waking up
            time_in_bed (int): desired number of hours in bed
        """
        self.have_work = have_work
        self.work_time = work_time
        self.commute = commute
        self.prep = prep
        self.time_in_bed = time_in_bed

    def departure(self):
        """Returns datetime object containing the time of departure.

        Calculates the time to be at work subtracted by the commute time and
        returns the necessary departure time required to arrive at work on
        time.

        ---
        departure time = time to arrive at work - commute time

        Returns:
            str: date in YYYY-MM-DD HH:MM:SS format
        """
        commute_object = timedelta(minutes=self.commute)
        work_time_object = datetime.strptime(self.work_time, "%B %d, %Y %I:%M %p")
        return work_time_object - commute_object

    def bed_time(self):
        """Returns datetime object containing the time to go to bed.

        Calculates the time to go to bed based on the time necessary to depart
        to work subtracted by the sum of preparation time and hours desired in
        bed.

        ---
        bed_time = departure time - (preparation time + time in bed)

        Returns:
            str: date in MMMM DD, YYYY HH:MM AM/PM format
        """
        prep_object = timedelta(hours=self.prep)
        time_in_bed_object = timedelta(hours=self.time_in_bed)
        commute_object = timedelta(minutes=self.commute)
        work_time_object = datetime.strptime(self.work_time, "%B %d, %Y %I:%M %p")
        return datetime.strftime(
            ((work_time_object - commute_object) - (prep_object + time_in_bed_object)),
            "%B %d, %Y %I:%M %p",
        )  # displays bed_time in 'MMMM DD, YYYY T:TT AM' format

    def wake_up(self):
        """Returns datetime object containing the time to wake up.

        Calculates the time to wake up based on subtracting preparation time from departure time.
        ---
        wake up time = departure time - preparation time

        Returns:
            str: date in MMMM DD, YYYY HH:MM AM/PM format
        """
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
