from manage import celery

@celery.task()
def celeryTest(a):
    print(a)
    return True
