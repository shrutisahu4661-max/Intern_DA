# Grade Calculator
A simple Python program that takes a student's name and marks, then outputs their grade with a motivational message.

# to Run
python grade_calculator.py

1. Enter student name
2. Enter marks (0-100)
3. Get grade and message

# Grading Scale

=> Grade - A, B, C, D, F
=> Range - 90-100, 80-89, 70-79, 60-69, 0-59

## Why I Did Things This Way

--Why conditional ranges like 90 <= marks <= 100
- More readable than marks >= 90 and marks <= 100
- Easier to verify correct boundaries at a glance

--Why return grade and message together?
- Keeps related data bundled
- Makes printing cleaner in main loop

--Why the infinite loop?
- Program keeps asking until valid input is given
- User gets multiple chances to correct mistakes

--Why convert name to uppercase in output?
- Makes results look cleaner and more formal
- Simple transformation, big visual impact

--Why try/except for marks input?
- Catches non-number inputs like "abc" or "95.5"
- Prevents program from crashing on bad data

## Project Structure

grade_calculator.py  # Main file
README.md            # Details
test_cases.txt       # Test info
screenshots.pnd      # screenshort of program inputs