import schedule
import time
from public.tracking import updateAllURLStatus


schedule.every(30).seconds.do(updateAllURLStatus)

while True:
    schedule.run_pending()
    time.sleep(1)
