put_time = float((input("What time is it? in hours.min:  ")))
match put_time:
    case _ if  put_time == 0.00:
        time = "Midnight"
    case _ if  put_time < 4.00:
        time = "Night"
    case _ if put_time < 06.00:
        time = "Dawn"
    case _ if put_time < 12.00:
        time = "Morning"
    case _ if put_time == 12.00:
        time = "Noon"
    case _ if put_time < 15.00:
        time = "midnight"
    case _ if put_time < 17.00:
        time = "Dusk"
    case _:
        time = "Night"
print("This time is called ", time)
    