# AHT20 temperature and humidity sensor

Status: draft integration. Current-stack hardware validation is pending.

This profile describes an AHT20 sensor connected to Axiom over I²C.
It provides temperature in degrees Celsius and relative humidity in percent.

## Profile details

- Device type: AHT20
- I²C address: 0x38
- Saved Axiom polling interval: 500 ms
- Detection: address-based; this profile has no identity-register check

An address match alone does not establish the attached sensor model.
The polling interval is separate from browser publication frequency.

## Hardware setup

Complete this section for the exact hardware used before recommending
this integration:

- Axiom model:
- Sensor breakout-board manufacturer and model:
- Product or datasheet link:
- Supply voltage and logic levels:
- Axiom connector or port:
- Wiring table or labelled photograph:

## Software requirements

Use firmware supporting Axiom's Device Library and a desktop browser
supporting Web Serial, such as Chrome or Edge.

The exact firmware, browser and operating-system versions used must be
recorded in the test report.

## Installation and testing

After the hardware setup above has been documented and checked:

1. Open the Device Library and connect Axiom.
2. Export the existing custom library if one is present.
3. Use Install → Reset draft from Axiom to retain existing custom entries.
4. In Advanced JSON, import this folder's profile.json.
5. Review any same-name replacement and the proposed library changes.
6. Write the library, restart Axiom, reconnect and refresh.
7. Inspect the boot result, including rejected entries and errors.
8. Open Test & tune, scan for the sensor and start readings.
9. Record several temperature and humidity readings, including startup
   behaviour, and check operation after another restart.

Writing replaces the complete custom library file. Restarting applies it.

AHT20 may already be included in the selected firmware. Record whether
this installation adds support or customises an existing type.

## Test evidence

[AHT20 test report, 2026-11-11](test-results/2026-11-11-nikos.md):
installation and the active custom override were verified on Axiom018,
firmware version 1. Temperature readings were approximately 19°C.
Humidity remained saturated at 100% with both the built-in and custom
definitions. Overall result: partial; cause unresolved.

Historical AHT20 tests exist in axiom-web-updater's Device Library
documentation. They used earlier firmware combinations and do not
establish compatibility with every current stack.

## Feedback

Include the exact sensor board, profile commit, firmware version,
reproduction steps and observed results when reporting a problem.