# Questions for Django Trainee at Accuknox

This repository contains answers to the Django Trainee assessment questions, including explanations and code snippets.

## **Questions & Answers**

### **1. Are Django signals executed synchronously or asynchronously by default?**
- By default, Django signals are executed synchronously.  
- See the provided code snippet in `que1_django_synchronous_signals.py` and `que1_django_asynchronous_signals.py` for proof.

### **2. Do Django signals run in the same thread as the caller?**
- Yes, Django signals run in the same thread as the caller.
- Check `que2_django_signals.py` for a code demonstration.

### **3. Do Django signals run in the same database transaction as the caller?**
- By default, Django signals run within the same database transaction.
- A detailed code snippet is available in `que3_django_signals.py`.

### **4. Implementing a `Rectangle` Class**
- I created a `Rectangle` class with the following requirements:
  - Requires `length: int` and `width: int` during initialization.
  - Supports iteration over an instance.
  - Returns length in the format `{'length': <VALUE>}` followed by width as `{'width': <VALUE>}`.

- The solution is available in `custom_classes.py`.
