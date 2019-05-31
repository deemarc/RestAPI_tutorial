"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

data = {'seconds':1}
def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    if 'seconds' in data:
        print('have second')
    
    if 'minute' in data:
        print('have minute')

    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', **data)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            print("hello from the main task")
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()