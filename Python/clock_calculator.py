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
        print(str(sum_minute))
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
        if sum_hour > 23:
            hour = sum_hour - 24
        else:
            hour = sum_hour
        sum_hour += minute_hour_change
        return sum_hour

    def print_time(self, hour=int, minute=int):
        output_time = str(hour) +":" + str(minute)
        print("Output time: " + output_time)


def parse_args(args):
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser = argparse.ArgumentParser(
        description="Takes in hour and minute and delta hour and minute."
    )
    parser.add_argument("-ho","--hour",help="Start hour value: hh", type=int, default="00")
    parser.add_argument("-mi","--minute",help="Start minute value: mm", type=int, default="00")
    parser.add_argument("-ah","--addhour", help="Input hour value to add: hh", type=int, default="00")
    parser.add_argument("-am","--addminute", help="Input minute value to add: mm", type=int, default="00")
    parser.add_argument("-sh","--subtracthour", help="Input hour value to subtract: mm", type=int, default="00")
    parser.add_argument("-sm","--subtractminute", help="Input minute value to subtract: mm", type=int, default="00")
    return parser.parse_args(args)



def main():
    args = parse_args(sys.argv[1:])
    args_dict = vars(args)

    timestamp = TimeStamp(**args_dict)

    print("startMin: " + str(args.minute))
    print("startHr: " + str(args.hour))
    print("addMin: " + str(args.addminute))
    print("addHr: " + str(args.addhour))
    minute = timestamp.add_minute(args.minute, args.addminute)
    hour = timestamp.add_hour(args.hour, args.addhour, minute[0])

    if len(str(hour)) <2:
        output_hour = "0" + str(hour)
    else:
        output_hour = str(hour)
    if len(str(minute)) <2:
        output_minute = "0" +str(minute[1])
    else:
        output_minute = str(minute[1])

    timestamp.print_time(output_hour,output_minute)


if __name__ == "__main__":
    main()