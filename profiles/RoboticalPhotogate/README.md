# Photogate

Photogate from Robotical, contributed from the Axiom Device Library.

## Profile details

- Device type: RoboticalPhotogate
- I²C address: Not set
- Saved Axiom polling interval: 100 ms
- Detection: identity check `=p250&0x00=0x0125`
- Values: gate1Raw (counts), gate2Raw (counts)

## Hardware setup

- Sensor breakout-board manufacturer and model: Axiom dual IR photogate (STM32F030K6)

### Wiring

Connect the photogate to Axiom using its RSAO add-on connector.

## Setup

Flash photogate_all.hex onto the photogate over SWD. Install the profile on Axiom and restart Axiom.

## Expected behaviour

gate1Raw and gate2Raw, each from 0 to 4095 ADC counts. Blocking either beam should lower its corresponding reading.

## Source and attribution

Written by the contributor for this library.

## Test evidence

Not yet tested on hardware. To add a result, copy test-results/TEMPLATE.md to a dated file.

## Feedback

Report results or problems in the [library's issues](https://github.com/robotical/axiom-device-library/issues).
