from celery import shared_task
import time

@shared_task
def test_task():
    time.sleep(5)
    print("Test task completed successfully!")
    return "Task finished"
