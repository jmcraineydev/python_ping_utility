import schedule
import time
from public.tracking import updateAllURLStatus


schedule.every(20).minutes.do(updateAllURLStatus)

while True:
    schedule.run_pending()
    time.sleep(1)
