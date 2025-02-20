# If signals were asynchronous, the main flow wouldn’t wait for the signal to finish.

import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Dummy model for demonstration
class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler for asynchronous execution
@receiver(post_save, sender=DummyModel)
def signal_test_asynchronous(sender, instance, **kwargs):
    def run_signal():
        print("Signal Started")
        time.sleep(5)  # Non-blocking delay
        print("Signal Completed")

    threading.Thread(target=run_signal).start()  # Runs in a separate thread

# Simulating model save action
if __name__ == "__main__":
    print("Creating object...")
    obj = DummyModel(name="Test")  
    post_save.send(sender=DummyModel, instance=obj)  # Manually triggering the signal
    print("Object Created!")

# Output

# Creating object...
# Signal Started  
# Object Created!  (Printed immediately)
# (Script pauses for 5 seconds...)
# Signal Completed  

