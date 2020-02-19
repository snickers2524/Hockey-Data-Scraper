def date_time_parser(date_time):
    date = date_time[0:10]
    time = date_time[11:19]
    return date + " " + time


