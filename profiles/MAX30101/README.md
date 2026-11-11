# MAX30101 — Heart Sensor

Draft integration migrated from Axiom's seed catalogue. No current-stack hardware test
is claimed here. The descriptor was copied without changes; source revision and original
compiled-library hash are recorded in [metadata.json](metadata.json).

## Descriptor requirements

- Manufacturer recorded by the descriptor: Vishay
- Possible I²C addresses: `0x57`
- Saved Axiom polling interval: 200 ms
- Declared reading fields: `Red` (Red), `IR` (IR)

These are descriptor declarations, not measured results. An address match alone does not
identify a sensor or establish that its initialization and readings work.

Catalogue eligibility: Eligible to add under the current Catalogue policy. This is not a hardware test result.

## Hardware and software setup

Before testing, identify the exact breakout board, supply voltage, logic levels and wiring.
Confirm compatibility with Axiom's connector and document the slot used. Those details have
not been established by this migration; follow the board manufacturer's documentation.
Use Axiom firmware with Device Library support and a desktop browser supporting Web Serial.
Record exact firmware, board, browser and OS versions in the test report.

## Try the integration

1. Connect Axiom and export any existing custom library as a backup.
2. In Install, use Reset draft from Axiom to retain existing custom entries.
3. Find `MAX30101` in Catalogue and choose Add to draft when it is eligible. Alternatively,
   import [profile.json](profile.json) through Advanced JSON. Read all restriction messages.
4. Review the draft and any same-name replacement. Writing replaces the complete custom file.
5. Write, restart, reconnect and refresh; inspect the boot result and rejected entries.
6. In Test & tune, scan and record identity checks, startup and subsequent readings.
7. Check a known stimulus or reference where applicable, then restart and check again.
8. Restore your backup if needed. Save successful, partial or failed observations using
   [the test-report template](test-results/TEMPLATE.md) and link the report from metadata.json.

A built-in definition with the same name can remain a fallback. File acceptance does not
prove the custom definition identified the device or produced correct readings.

## Feedback and attribution

Open an issue or PR with the profile commit, exact hardware/software combination, steps and
observations. Preserve existing reports and attribution. This profile was copied from
Robotical's ISC-licensed axiom-web-updater; see metadata.json and the repository licence.
