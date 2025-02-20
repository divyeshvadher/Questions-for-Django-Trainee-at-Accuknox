# Yes, by default, Django signals run in the same thread as the caller. This means that when a signal is triggered, it executes immediately and blocks the execution of the main thread until it completes.

# To prove this, we will print the thread name of both the main execution and the signal handler. If Django signals were running in a separate thread, the thread names would be different.

import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Dummy model for testing
class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=DummyModel)
def signal_test(sender, instance, **kwargs):
    print(f"Signal Started in thread: {threading.current_thread().name}")
    time.sleep(3)  # Adding delay to observe behavior
    print("Signal Completed")

# Simulating model save action
if __name__ == "__main__":
    print(f"Creating object in thread: {threading.current_thread().name}")
    obj = DummyModel(name="Test")  
    post_save.send(sender=DummyModel, instance=obj)  # Manually triggering the signal
    print("Object Created!")


# Expected Output

# Creating object in thread: MainThread
# Signal Started in thread: MainThread
# (Script pauses for 3 seconds...)
# Signal Completed
# Object Created!


