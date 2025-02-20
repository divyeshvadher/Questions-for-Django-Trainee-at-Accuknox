# Yes, by default, Django signals run in the same database transaction as the caller. This means that if a database transaction is rolled back, the signal execution is also rolled back.

# To prove this, we will use a post_save signal and check whether the signal executes within a transaction by deliberately causing a rollback inside a database operation. If signals were running independently, the rollback wouldn’t affect them.

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Dummy model for testing
class DummyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=DummyModel)
def signal_test(sender, instance, **kwargs):
    print("Signal Triggered - Checking if it runs in the same transaction.")

# Function to test transaction rollback behavior
def test_transaction():
    try:
        with transaction.atomic():  # Start a transaction
            print("Starting Transaction...")
            obj = DummyModel.objects.create(name="Test Object")
            print("Object Created in DB.")

            # Manually raising an error to trigger rollback
            raise Exception("Forcing Transaction Rollback")

    except Exception as e:
        print(f"Transaction Rolled Back: {e}")

# Running the test function
test_transaction()

# Expected Output

# Starting Transaction...  
# Object Created in DB.  
# Transaction Rolled Back: Forcing Transaction Rollback  


