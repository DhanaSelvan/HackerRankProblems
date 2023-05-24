def time_conversion(s):
    time = s.split(":")
    time_suffix = time[-1][2::]
    if(time_suffix == ("AM" or "am") and time[0] == "12"):
        time[0] = "00"
    elif(time_suffix == ("AM" or "am")):
        time[0] = time[0]
    elif(time_suffix == ("PM" or "pm") and time[0] == "12"):
        time[0] = "12"
    else:
        time[0] = str(int(time[0]) + 12)
        
    time1 = time[0:2]
    time_sec = time[-1][0:2]
        
    return (":".join(time1) + ":" + time_sec)

s = str(input())
convert = time_conversion(s)
print(convert)