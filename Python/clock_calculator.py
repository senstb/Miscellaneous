import argparse
import sys

class TimeStamp(object):
    def __init__(self, **kwargs):
        self.starthour = kwargs.get("starthour")
        self.startminute = kwargs.get("startminute")
        self.addhour = kwargs.get("addhour")
        self.addminute = kwargs.get("addminute")
  

    def add_minute(self, startminute=int, addminute=int):
        return_minute_object = [0,startminute]
        sum_minute = startminute + addminute
        if sum_minute > 59:
            return_minute_object[1] = sum_minute - 60
            return_minute_object[0] = 1
        if sum_minute < 0:
            return_minute_object[1] = sum_minute + 60
            return_minute_object[0] = -1
        else:
            return_minute_object[1]= sum_minute
        return return_minute_object
    

    def add_hour(self, starthour=int, addhour=int, minute_hour_change=int):
        sum_hour = starthour + addhour
        sum_hour += minute_hour_change

        if sum_hour > 23:
            hour = sum_hour - 24
        elif sum_hour <0:
            hour = sum_hour + 24
        else:
            hour = sum_hour
        return sum_hour

    def print_time(self, hour=int, minute=int):
        output_time = str(hour) +":" + str(minute)
        print("Output time: " + output_time)


def parse_args(args):
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser = argparse.ArgumentParser(
        description="Takes in hour and minute and delta hour and minute."
    )
    parser.add_argument("-ho","--hour",help="Start hour value: hh", nargs='?')
    parser.add_argument("-mi","--minute",help="Start minute value: mm",  nargs='?')
    parser.add_argument("-ah","--addhour", help="Input hour value to add: hh", nargs='?')
    parser.add_argument("-am","--addminute", help="Input minute value to add: mm", nargs='?')
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    args_dict = {}
    if None not in vars(args).viewvalues():
        args_dict = vars(args)
    else:
        args_dict["hour"] = input("Starting hour: ")
        args_dict["minute"] = input("Starting minute: ")
        args_dict["addhour"] = input("Change in hour: ") 
        args_dict["addminute"] = input("Change in minute: ")


    timestamp = TimeStamp(**args_dict)

    print("startMin: " + str(args_dict["minute"]))
    print("startHr: " + str(args_dict["hour"]))
    print("addMin: " + str(args_dict["addminute"]))
    print("addHr: " + str(args_dict["addhour"]))

    minute = timestamp.add_minute(args_dict["minute"], args_dict["addminute"])
    hour = timestamp.add_hour(args_dict["hour"], args_dict["addhour"], minute[0])

    if len(str(hour)) <2:
        output_hour = "0" + str(hour)
    else:
        output_hour = str(hour)
    if len(str(minute[1])) <2:
        output_minute = "0" + str(minute[1])
    else:
        output_minute = str(minute[1])

    timestamp.print_time(output_hour,output_minute)


if __name__ == "__main__":
    main()