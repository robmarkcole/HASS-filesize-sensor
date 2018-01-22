# HASS-database-sensor
Custom component for displaying the size of the HA [database file](https://home-assistant.io/docs/backend/database/), as described in [this feature request](https://community.home-assistant.io/t/database-size-sensor/40303)

## Motivation
There are quite a few posts where people want to know the size of their HA database on disk. This custom component creates a sensor which displays the size in MB of the db file. In future other statistics can be recorded in attributes.

## Usage
Add the contents of **custom_components/sensors** to your config. Edit the absolute path to your database in the **database.py** file.
Add the following to your config:

```yaml
sensor:
  - platform: database
  ```
