# Design Decisions for Exercise 1: Analog Input

## Photocell Setup:
Implemented a voltage divider with a 10k ohm resistor to connect the photocell to ADC2 (GP28). This converts light intensity into analog voltage readings that we can use to adjust LED brightness.

## Calibration Values:
After testing, set `max_bright = 20000` for bright conditions and `min_bright = 10000` for dim conditions. These values were chosen to calibrate the LED’s response to different light levels.

## LED Control:
Used `machine.Pin` to toggle the onboard LED brightness based on the light sensor input.  
Implemented a `clip()` function to ensure that the calculated duty cycle remains within the valid range `[0, 1]`.

## Loop Logic:
The code reads the analog value from the photocell, calculates the corresponding duty cycle, and uses it to adjust the on/off timing of the LED to simulate brightness changes.

# Design Decisions for Exercise 2: PWM Sound Output

## PWM Setup:
- Used GP16 for PWM output to the speaker.
- Connected the speaker's black wire to GND and red wire to GP16.

## Tone Generation:
- Created a dictionary of note frequencies for *Für Elise*.
- Used `playtone()` to generate tones by setting PWM frequency and duty cycle.
- Turned off the speaker between notes with `quiet()`.

## Melody Logic:
- Stored the melody as a list of notes and durations.
- Played each note for its duration, with short pauses in between.

## Future Considerations:
- Amplification and additional hardware could improve sound output.
