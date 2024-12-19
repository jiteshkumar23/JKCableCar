import datetime

from config import visitDate

# Your input dates in the format YYYY-MM-DD
input_visit_date = visitDate


# Convert the input dates to datetime objects at midnight UTC
date1 = datetime.datetime.strptime(input_visit_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc, hour=0,
                                                                           minute=0, second=0, microsecond=0)

# Convert the datetime objects to timestamps in milliseconds
visit_timestamp = int(date1.timestamp() * 1000)

print(f"checkin date {input_visit_date} converted to millis is --> {visit_timestamp}")
