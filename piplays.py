# Imports
import keyboard as k
import os
import time as t
import mmap
import sys
import tkinter as tk

# Gathers the digits
def digit_gather(pi_file):
    print("Translating")
    # Check if file exists before trying to open it
    if not os.path.exists(pi_file):
        print("File not found, file might be corupted.")
    
    with open(pi_file, 'rb') as f:
        # Memory map the file - this doesn't load it all into RAM
        mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    return mmapped_file

def get_pi_digit(pi_map, position):
    actual_position = position + 2
    # Make sure position is within bounds
    if actual_position >= pi_map.size():
        print("Reached end of file. Restarting from beginning.")
        actual_position = 2 
    
    # Get the character at the position
    pi_map.seek(actual_position)
    digit = pi_map.read(1).decode('utf-8')
    # Skip any non-digit characters that might be in the file
    while not digit.isdigit() and actual_position < pi_map.size():
        actual_position += 1
        pi_map.seek(actual_position)
        digit = pi_map.read(1).decode('utf-8')
    return digit

def keytest():
    k.press_and_release('q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0')
    if k.is_pressed('a'):  # Using is_pressed to check a key as an example
        print("Success")
    else:
        print("Incompatible keyboard layout. Please ensure that this is running with an EN-US keyboard.")

def start():
    global current_position
    print("Starting...")
    
    # Setup escape key before the sleep
    k.add_hotkey('esc', lambda: sys.exit())
    
    # First sleep
    print(f"Waiting for 20 seconds before checking digits...")
    t.sleep(20)  # Removed quotes - this should be a number, not a string
    
    # Start checking digits
    while True:
        pi_digit = get_pi_digit(pi_map, current_position)
        print(f"Position {current_position}: Digit is {pi_digit}")
        current_position += 1  # Increment position for next call
        
        if pi_digit == '0':  # Compare to string '1', not integer 1
            k.press("w")
            t.sleep(0.1)
            k.release("w")
        
        if pi_digit == '1':  # Compare to string '1', not integer 1
            k.press("a")
            t.sleep(0.1)
            k.release("a")
            
        if pi_digit == '2':  # Compare to string '1', not integer 1
            k.press("s")
            t.sleep(0.1)
            k.release("s")
        
        if pi_digit == '3':  # Compare to string '1', not integer 1
            k.press("d")
            t.sleep(0.1)
            k.release("d")

        if pi_digit == '4':  # Compare to string '1', not integer 1
            k.press("q")
            t.sleep(0.1)
            k.release("q")

        if pi_digit == '5':  # Compare to string '1', not integer 1
            k.press("e")
            t.sleep(0.1)
            k.release("e")

        if pi_digit == '6':  # Compare to string '1', not integer 1
            k.press("z")
            t.sleep(0.1)
            k.release("z")

        if pi_digit == '7':  # Compare to string '1', not integer 1
            k.press("x")
            t.sleep(0.1)
            k.release("x")

        if pi_digit == '8':  # Compare to string '1', not integer 1
            k.press("c")
            t.sleep(0.1)
            k.release("c")

        if pi_digit == '9':  # Compare to string '1', not integer 1
            k.press("v")
            t.sleep(0.1)
            k.release("v")

        t.sleep(1)  # Small delay between checks

# Main code
pi_file_path = "pi.txt"
pi_map = digit_gather(pi_file_path)  # Use the pi_file_path variable
current_position = 0

# Start the program
start()
