#!/usr/bin/env python3
"""
PWM Tone Generator
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

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


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


print("Fur Elise:")

for note, duration in melody:
    freq = int(NOTES[note])
    print(f"Playing note: {note}")
    playtone(freq, duration)
    quiet()  # Turn off the speaker between notes
    utime.sleep(0.05)  # Short pause between notes

# Turn off the PWM
quiet()
