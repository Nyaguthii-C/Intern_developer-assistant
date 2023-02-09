
## Technical assesment Alx-internship
### problem_0.py
You are preparing a cake but you dont know how many teaspoons of sugar you will need to make it "perfect" or "not too sweet".
in this case, find the first number of teaspoons that will make the cake "too sweet". For the first check, you add *n* teaspoons of sugar but it's too sweet to your taste. UUnfortunately, you can’t rollback to a previous version of your cake by taking out teaspoons of sugar to adjust the sweetness to your cake. However, you do have a tool to indicate if the current number of teaspoons of sugar will make your cake too sweet. You want to redo this cake but to do so, you need to know at which point the number of teaspoons of sugar will make your cake too sweet.
You are given n, the number of teaspoons of sugar that the recipe states is required to make your cake and a function isTooSweet(i), which returns true if i teaspoons of sugar makes your cake too sweet. With these two pieces of information, find x, the first number of teaspoons of sugar that will make your cake too sweet.

**Extra clarifications:** 

After x the cake is too sweet
n is superior or equal to 1
For any value of n, your cake will be always too sweet (x always exists)

### problem_1.py
Imagine you have a special keyboard with the following keys:
Key 1: (A): Print one ‘A’ on screen
Key 2: (Ctrl-A): Select everything printed in the whole screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
You can only press the keyboard for N times, find out the maximum numbers of ‘A’ you can print on screen.
Example 1:
Input: N = 2
Output: 2 -> for the sequence: A, A
Example 2:
Input: N = 7
Output: 9 -> for the sequence: A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V

**Extra clarifications:**

1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

### problem_2.py

You are the new owner of a wheat farm and you want to put in place an automated water distribution. You have multiple wheat fields and water towers dispatched to your farm. You want to know what’s the maximum distance between a field and a water tower for buying the right water pump: not too powerful because it's too expensive and also not too weak.
You can modelize fields and water towers by 2 lists of integers, each integer representing the position. You can assume the field and water towers are in the same “line”. The maximum distance between a field and a tower will be the pump power needed.
Write a function that returns the max power needed for the list of fields and water towers.

**Extra clarification:** 

Each list are sorted
List can’t be empty
Positions are non-negative integer
The max value of a position is 10^9
Examples below if the candidate needs more cases
Example 1:
Fields = [1, 2, 3]
Towers = [2] => Max distance: 1
Example 2:
Fields = [1, 2, 3, 4]
Towers = [1, 4] => Max distance: 1
Example 3:
Fields = [1, 5]
Towers = [10] => Max distance: 9
