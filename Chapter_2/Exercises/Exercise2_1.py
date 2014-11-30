"""
Exercise 2.1
------------------------------------------
Another Ball Dropped From a Tower
------------------------------------------
Function: The program finds the time it
      takes for the ball to reach the
      ground.

Input: The user inputs the height of the
      tower.

Output: The program outputs the time for
      the ball to reach the ground.

"""

# User inputs the height
h = float(raw_input('Enter the height of the tower: '))

# Time taken to reach the bottom
g = 9.81 #meters/seconds**2
t = (2*h/g)**(0.5) #seconds

# Print the height based on user parameters
print 'It takes', t, 'seconds to reach the ground.'