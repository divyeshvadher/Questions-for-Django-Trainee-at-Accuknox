# By default, Django signals run synchronously, meaning they execute immediately within the same thread before the next operation continues.

# To prove this, let's take a simple example where we define a post_save signal and introduce a delay inside the signal handler. 

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Dummy model for demonstration
class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler for synchronous execution
@receiver(post_save, sender=DummyModel)
def signal_test_synchronous(sender, instance, **kwargs):
    print("Signal Started")
    time.sleep(5)  # Blocking execution for 5 seconds
    print("Signal Completed")

# Simulating model save action
if __name__ == "__main__":
    print("Creating object...")
    obj = DummyModel(name="Test")  
    post_save.send(sender=DummyModel, instance=obj)  # Manually triggering the signal
    print("Object Created!")

# Output:

# Creating object...
# Signal Started  
# (Script pauses for 5 seconds...)
# Signal Completed  
# Object Created!
