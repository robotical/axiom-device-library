# Axiom Device Library

Shared device profiles, setup guides, examples and test results for Axiom.

## Integrations

These 35 profiles were copied from the existing Axiom Catalogue. Migration preserves the
descriptors; it does not establish hardware compatibility. Integrations remain draft and
compatibility claims apply only to the combinations in their test reports.

| Integration | Purpose | Status |
|---|---|---|
| [AdafruitGamepad](profiles/AdafruitGamepad/README.md) | Adafruit Gamepad | Draft |
| [AdafruitSoilSensor](profiles/AdafruitSoilSensor/README.md) | Soil Moisture Sensor | Draft |
| [ADXL313](profiles/ADXL313/README.md) | Accelerometer | Draft |
| [AHT20](profiles/AHT20/README.md) | Temperature & Humidity Sensor | Draft |
| [AMG8833](profiles/AMG8833/README.md) | Thermal Camera | Draft |
| [AS5600](profiles/AS5600/README.md) | Magnetic Encoder | Draft |
| [CAP1203](profiles/CAP1203/README.md) | Capacitive Touch | Draft |
| [GravityO2](profiles/GravityO2/README.md) | Oxygen Sensor | Draft |
| [HX711](profiles/HX711/README.md) | Force Sensor | Draft |
| [LPS25](profiles/LPS25/README.md) | Pressure Sensor | Draft |
| [LSM6DS](profiles/LSM6DS/README.md) | Accelerometer & Gyroscope | Draft |
| [LTR-329](profiles/LTR-329/README.md) | Light Sensor (IR and visible) | Draft |
| [LTR-390](profiles/LTR-390/README.md) | Light Sensor (UV and visible) | Draft |
| [M5-Weight](profiles/M5-Weight/README.md) | Weight Sensor | Draft |
| [M5Encoder](profiles/M5Encoder/README.md) | Rotary Encoder | Draft |
| [MAX17048](profiles/MAX17048/README.md) | Battery Fuel Gauge | Draft |
| [MAX30101](profiles/MAX30101/README.md) | Heart Sensor | Draft |
| [MCP9808](profiles/MCP9808/README.md) | Temperature Sensor | Draft |
| [MMC5603](profiles/MMC5603/README.md) | Magnetometer | Draft |
| [MPRLS](profiles/MPRLS/README.md) | Pressure Sensor | Draft |
| [MXC400xXC](profiles/MXC400xXC/README.md) | Accelerometer | Draft |
| [QwiicButton](profiles/QwiicButton/README.md) | QWIIC Button | Draft |
| [QwiicLEDStick](profiles/QwiicLEDStick/README.md) | RGB LED Stick | Draft |
| [SCD30](profiles/SCD30/README.md) | CO2 Sensor | Draft |
| [SCD40](profiles/SCD40/README.md) | CO2 Sensor | Draft |
| [SGP30](profiles/SGP30/README.md) | Gas Sensor (VOC) | Draft |
| [SGP40](profiles/SGP40/README.md) | SGP40 | Draft |
| [SHT40](profiles/SHT40/README.md) | Temperature & Humidity Sensor | Draft |
| [STCC4](profiles/STCC4/README.md) | CO2 Sensor | Draft |
| [TMP117](profiles/TMP117/README.md) | Temperature Sensor | Draft |
| [VCNL4040](profiles/VCNL4040/README.md) | Light Sensor (ambient & proximity) | Draft |
| [VL53L0X](profiles/VL53L0X/README.md) | Distance Sensor | Draft |
| [VL53L1X](profiles/VL53L1X/README.md) | Distance Sensor | Draft |
| [VL53L4CD](profiles/VL53L4CD/README.md) | Distance Sensor | Draft |
| [VL6180](profiles/VL6180/README.md) | Distance Sensor | Draft |

AHT20's existing documentation and test work are preserved. Its worked-example PR records
partial results, including unresolved humidity saturation; migration adds no verification claim.

## Catalogue publication

This repository is the source for shared profiles. The private Device Library service reads
only `main`, caches a complete commit and serves the Catalogue to the web application.
Open PRs appear in Community and are not installed or published as Catalogue changes.
After a reviewed PR merges, a signed webhook queues refresh; periodic reconciliation covers
missed events. GitHub or validation failures retain the last good snapshot.

Rollout of this connection is coordinated with the private service and web updater; until
those changes deploy, the existing website still uses its previous static catalogue.

See [CONTRIBUTING.md](CONTRIBUTING.md) for feedback, contribution and review instructions.
The repository uses the [ISC licence](LICENSE). Contributors retain their copyright.
