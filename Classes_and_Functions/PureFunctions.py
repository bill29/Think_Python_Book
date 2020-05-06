class Time:
    """
    Represents the time of day
    attributes : hour, minute, second
    """
    def show_time(self):
        print(self.hour,':',self.minute,':',self.second)
# here is a simple prototype od add_time:
# This is called a pure function because it does not modify any of the objects
# passed to it as arguments and it has no effect, like displaying a value or getting user input,
# other than returning a value.
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum
start = Time()
start.hour = 9
start.minute = 20
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print(done.hour,':',done.minute,':',done.second)

"""
The problem is that this function does not deal with cases where the number of seconds or minutes adds up to more than sixty
"""

#improved version:
def add_time2(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second>60:
        sum.second -=60
        sum.minute +=1

    if sum.minute>60:
        sum.minute -=60
        sum.hour +=1
    return sum
done2 = add_time2(start, duration)
done2.show_time()

#debugging
def time_to_int(time):
    minutes = time.hour*60 + time.minute
    seconds = minutes*60
    return seconds
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def valid_time(time):
    if time.hour <0 or time.minute<0 or time.second<0:
        return False
    if time.minute >60 or time.second>60:
        return False
    return True
def add_time3(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    # assert statement
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

time_done = add_time3(start, duration)
print('Final time:')
time_done.show_time()
