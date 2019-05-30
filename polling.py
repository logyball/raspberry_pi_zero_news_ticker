from time import sleep
import google_news_headlines as gnh
import weather

while True:
    local = gnh.get_local()
    national = gnh.get_national()
    wet = weather.get_weather()
    print("Local News:")
    print(local)
    print("National News:")
    print(national)
    print("Current Weather:")
    print(wet)
    sleep(5)