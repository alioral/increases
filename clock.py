from apscheduler.scheduler import Scheduler
import requests

sched = Scheduler()

@sched.interval_schedule(seconds=5)
def timed_job():
    r = requests.get('http://increases.herokuapp.com/updatePages')
    print "Pages update code: " + r.status_code

sched.start()

while True:
    pass