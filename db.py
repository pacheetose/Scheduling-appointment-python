import time
cutime = [time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_year]
tm = "{}-{}-{}".format(cutime[0],cutime[1],cutime[2])
print(tm)