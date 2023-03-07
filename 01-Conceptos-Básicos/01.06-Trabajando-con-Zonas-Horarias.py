from datetime import datetime, timedelta, timezone  
from pytz import timezone
import pytz

# Mostrar las zonas horarias disponibles
#print(pytz.all_timezones)
#print(type(pytz.all_timezones))

# Mostrar la fecha actual

dt = datetime.now()
print(dt)
print("")
print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("Europe/Madrid")))
print(datetime.now(pytz.timezone("US/Alaska")))
print(datetime.now(pytz.timezone("UTC")))
