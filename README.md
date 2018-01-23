# HASS-filesize-sensor
Custom component for displaying the size of a files. Discussion on [this thread](https://community.home-assistant.io/t/database-size-custom-component/40308).

## Motivation
There are quite a few posts where people want to know the size of a file, for example their HA database file. This custom component creates sensors which displays the size of a files in MB. The configured file path for a sensor is displayed as an attribute.

## Usage
Add the contents of **custom_components/sensors** to your config.
Add absolute paths to your config following:

```yaml
# On Mac
sensor:
  - platform: filesize
    file_paths:
      - /Users/username/.homeassistant/home-assistant_v2.db
      - /Users/username/.homeassistant/home-assistant.log

# On Hassio or Docker (e.g. on a Synology NAS)
sensor:
  - platform: filesize
    file_paths:
      - /config/home-assistant_v2.db
  ```
