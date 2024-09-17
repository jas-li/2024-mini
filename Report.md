# Exercise 1
1. What are the "max_bright" and "min_bright" values you found?

max_bright = 11000
min_bright = 20000

# Exercise 2
What we modified the exercise_sound.py script to play Fur Elise by Beethoven 
```python 
# Dictionary of notes and their frequencies (in Hz)
NOTES = {
    'E5': float(659.25),
    'D#5': float(622.25),
    'B4': float(493.88),
    'D5': float(587.33),
    'C5': float(523.25),
    'A4': float(440.00)
}

# Melody: (note, duration) duration is in seconds
melody = [
    ('E5', 0.4),
    ('D#5', 0.4),
    ('E5', 0.4),
    ('D#5', 0.4),
    ('E5', 0.4),
    ('B4', 0.4),
    ('D5', 0.4),
    ('C5', 0.4),
    ('A4', 0.8) 
]

# Play Fur Elise
for note, duration in melody:
    freq = int(NOTES[note])
    print(f"Playing note: {note}")
    playtone(freq, duration)
    quiet()  # Turn off the speaker between notes
    utime.sleep(0.05)  # Short pause between notes
```

# Exercise 3
User Stories:
- As a player, I want to track my response time when the LED flashes so that I can test how fast my reaction speed is.
- As a player, I want the average, minimum, and maximum response time after playing 10 flashes total so I can get insights into my performance and identify areas for improvement.
- As a player, I want my statistics to be on FireBase so that I can view it another device.
