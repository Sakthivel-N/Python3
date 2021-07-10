def timeConversion(s):
    if (s.find("PM") >= 0):
        if (s[:2] != "12"):
            hrs=s[:2]
            val=int(hrs)
            hours = abs(int(val + 12))

            ti_zone = s.replace("PM", "")

            out = ti_zone.replace(ti_zone[:2], str(hours))
            return (out)
        else:
            out = s.replace("PM", "")
            return (out)

    else:
        if (s[:2] != "12"):
            out = s.replace("AM", "")
            return (out)

        else:
            ti_zone = s.replace("AM", "")
            out = ti_zone.replace(ti_zone[:2], "00")
            return (out)

