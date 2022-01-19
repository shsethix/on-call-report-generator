from datetime import datetime


UTC_datetime = datetime.utcnow()
UTC_datetime_timestamp = float(UTC_datetime.strftime("%s"))
print(UTC_datetime_timestamp)

local_datetime_converted = datetime.fromtimestamp(UTC_datetime_timestamp)

print(local_datetime_converted)