1. Parameter vs Argument
def deposit(amount):    # amount = parameter
    pass

deposit(200)            # 200 = argument

Parameter → variable that receives a value.
Argument → actual value supplied.




2. self
def change_name(self, name):

self refers to the current object/instance.

dog1.change_name("Max")

Conceptually:

self → dog1
name → "Max"



3. Local vs Instance Attribute
fee = 10          # local variable
self.balance = 50 # instance attribute

A local variable exists only within its function/method call.

An instance attribute belongs to an object and can later be accessed through it:

account.balance




4. Class Variables 🆕
class Student:
    school = "ABC"      # class variable

    def __init__(self, name):
        self.name = name

Remember:

Class variable      → belongs to CLASS
Instance attribute  → belongs to individual OBJECT
Local variable      → exists in function/method scope

Changing:

Student.school = "XYZ"

changes the class-level value.

But:

s1.school = "PQR"

creates/sets an instance attribute for s1, which shadows the class attribute.




5. Attribute Lookup 🆕

When Python sees:

s1.school

for this basic case, think:

Does s1 have school?
      ↓
YES → use it

NO
 ↓
Look at Student.school



6. @classmethod and cls 🆕
class Student:
    school = "ABC"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Important:

self → current OBJECT
cls  → current CLASS

cls does not mean class variable.

If cls → Student, then:

cls.school

means:

Student.school