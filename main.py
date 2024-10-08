def totalcalc(billamount,tippercent):
    total=billamount*(1+0.01*tippercent)
    total=round(total,2)
    print(f"please pay ${total}")
totalcalc(150,20)