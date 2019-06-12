from time import sleep
import google_news_headlines as gnh
import scrollphathd as sphd
import weather

local = []
national = []
wet = []

def build_whole_string():
    msg = '||| Local News: '
    local = gnh.get_local()
    national = gnh.get_national()
    wet = weather.get_weather()
    temp = str(int(wet.get('temp'))) + 'F ...'
    for i in range(len(local)):
        msg += str(i+1) + '. ' + local[i][0] +' ... Temp: ' + temp
    msg += ' ||| National News: '
    for i in range(len(national)):
        msg += str(i+1) + '. ' + national[i][0] + ' ... Temp: ' + temp
    return msg


while True:
    msg = build_whole_string()
    print(msg)
    sphd.clear()
    sphd.show()
    sphd.write_string(msg, brightness=0.3)
    for i in range(5000):
        sphd.show()
        sphd.scroll()
        sleep(0.015)