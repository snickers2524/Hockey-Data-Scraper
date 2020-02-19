import math

def time_change(mm_ss):
    if len(mm_ss) == 5:
        if math.floor(int(mm_ss[0:2]) / 60) >=1 & math.floor(int(mm_ss[0:2]) / 60) < 10:
            if int(mm_ss[0:2]) % 60>=10:
                hh_mm_ss = f"{'0' + str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
            else:
                hh_mm_ss = f"{'0' + str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + '0' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
        elif math.floor(int(mm_ss[0:2]) / 60) >=10:
            if int(mm_ss[0:2]) % 60>=10:
                hh_mm_ss = f"{str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
            else:
                hh_mm_ss = f"{str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + '0' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
        else:
            if int(mm_ss[0:2]) % 60 >= 10:
                hh_mm_ss = f"{'00' + str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
            else:
                hh_mm_ss = f"{'00' + str(math.floor(int(mm_ss[0:2]) / 60)) + ':' + '0' + str(int(mm_ss[0:2]) % 60) + ':' + mm_ss[3:5]}"
        return  hh_mm_ss
    else:
        return mm_ss