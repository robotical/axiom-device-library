# HX711 — Force Sensor

Draft integration migrated from Axiom's seed catalogue. No current-stack hardware test
is claimed here. The descriptor was copied without changes; source revision and original
compiled-library hash are recorded in [metadata.json](metadata.json).

## Descriptor requirements

- Manufacturer recorded by the descriptor: Avia
- Possible I²C addresses: not declared
- Saved Axiom polling interval: 100 ms
- Declared reading fields: `force` (N), `valid`

These are descriptor declarations, not measured results. An address match alone does not
identify a sensor or establish that its initialization and readings work.

Catalogue eligibility: No I²C addresses are supplied for this address-based catalogue.

## Hardware and software setup

Before testing, identify the exact breakout board, supply voltage, logic levels and wiring.
Confirm compatibility with Axiom's connector and document the slot used. Those details have
not been established by this migration; follow the board manufacturer's documentation.
Use Axiom firmware with Device Library support and a desktop browser supporting Web Serial.
Record exact firmware, board, browser and OS versions in the test report.

## Reference profile only on current firmware

This profile is retained to document the existing seed library. It cannot currently be added
under the Catalogue policy for the reason above. Do not use JSON import to bypass that restriction.

To help improve support, report the exact board, firmware, desired connection and any test
observations. A maintainer can then investigate the restriction and the required firmware or
profile changes. [The test-report template](test-results/TEMPLATE.md) is available for those
coordinated tests; this migration has not performed them.

## Feedback and attribution

Open an issue or PR with the profile commit, exact hardware/software combination, steps and
observations. Preserve existing reports and attribution. This profile was copied from
Robotical's ISC-licensed axiom-web-updater; see metadata.json and the repository licence.
