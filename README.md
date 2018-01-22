# HASS-filesize-sensor
Custom component for displaying the size of a file. Discussion on [this thread](https://community.home-assistant.io/t/database-size-custom-component/40308).

## Motivation
There are quite a few posts where people want to know the size of a file, for example their HA database file. This custom component creates a sensor which displays the size of a file in MB. The configured file path is displayed as an  attribute.

## Usage
Add the contents of **custom_components/sensors** to your config. Edit the absolute path to your file in **filesize.py**.
Add the following to your config:

```yaml
sensor:
  - platform: filesize
  ```
