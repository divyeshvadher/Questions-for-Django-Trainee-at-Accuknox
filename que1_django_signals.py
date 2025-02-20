import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Dummy model for demonstration
class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=DummyModel)
def signal_test(sender, instance, **kwargs):
    print("Signal Started")
    time.sleep(5)  # Adding delay to check synchronous behavior
    print("Signal Completed")

# Simulating model save action
if __name__ == "__main__":
    print("Creating object...")
    obj = DummyModel(name="Test")  
    post_save.send(sender=DummyModel, instance=obj)  # Manually triggering the signal
    print("Object Created!")
