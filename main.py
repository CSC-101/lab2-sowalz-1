# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("sowalz@calpoly.edu")
print(message)

#task 3
def smallest(n:float, m:float) -> float:
   if n < m:
      return n # For which calls below is this statement evaluated? A: neither
   else:
      return m

first = smallest(3,2) # What is the value of first? A: first = 2
second = smallest(2, 2) # What is the value of second? Is this a reasonable result? Why or why not?
# A: second = 2,  I don't think this is a reasonable result because a number cannot be less than itself
print()

def function2(a:int, b:int, c:int)-> int:
   if a > b and a > c:
      return a - b # In general, when will a call to this function evaluate this statement?
   # A: when the statement above evaluates to true
   elif b > c:
      return b + c # In general, when will a call to this function evaluate this statement?
   # A: when the first statement evaluates to false and the second statement evaluates to true
   else:
      return 2 * c # In general, when will a call to this function evaluate this statement?
   # A: when the first two statements evaluate to false

answer1 = function2(3,2,1) # What is the value of answer1? A: answer1 = 1
answer2 = function2(2,3,1) # What is the value of answer2? A: answer2 = 4
answer3 = function2(2,1,3) # What is the value of answer3? A: answer3 = 6
print()

#task 4
from typing import Optional

def checked_access(L:list[int], idx:int)-> Optional[int]:
   test = idx >= 0 and idx < len(L) # What is the value of test on each call? A: False, True
   if test: # What is this check preventing? A: Checks that the index is within the list
      return L[idx]
   else:
      return None

first = checked_access([1,0,1],9) # What is the value of first? A: None
second = checked_access([1,0,1],2) # What is the value of second? A: 1
print()

def length_sum(L:list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[2])
      # For which call below is this statement evaluated
      # and what are the values being added? A: call is first, values are length of "this" and "the"
   elif len(L) > 1:
      result = len(L[0]) + len(L[1])
      # For which call below is this statement evaluated
      # and what are the values being added? A: call is third, values are length of "another" and "call"
   elif len(L) > 0:
      result = len(L[0])
      # For which call below is this statement evaluated
      # and what are the values being added? call is second, value is length of "second call"
   else:
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
   # What is the value of words at this point? A: words = ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
   # What are the values of first and second at this point?
      # A: first = ["this", "is", "confusing", "code.", "AVOID"], second = ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
   # What happened? A: The function surprising appends a new element to the list words and saves each changed list to the variables first and second.
print()