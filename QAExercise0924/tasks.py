from invoke import task
import os
import threading


@task
def test(c, env='QA', marker='web'):
    markerList = marker.split(",")
    jobs = []
    for m in markerList:
        thread = threading.Thread(target=run_automation_test, args=(c, m, env))
        jobs.append(thread)
        thread.start()

    for thread in jobs:
        thread.join()

def run_automation_test(c, m, env):
    runningCommand = f"python3 -m pytest -m {m} ./src/testcases/web/* --env={env} "
    c.run(runningCommand)

