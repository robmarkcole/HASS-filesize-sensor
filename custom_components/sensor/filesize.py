"""
Sensor for checking the size of a file.
"""
import logging
import os
import voluptuous as vol

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA

_LOGGER = logging.getLogger(__name__)


CONF_FILE_PATHS = 'file_paths'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_FILE_PATHS): cv.ensure_list,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the file size sensor."""
    sensors = []
    for path in config.get(CONF_FILE_PATHS):
        _LOGGER.warning("File path: {}".format(path))
        sensors.append(Filesize(path))

    add_devices(sensors, True)


class Filesize(Entity):
    """Representation of the HA database."""
    ICON = 'mdi:file'

    def __init__(self, path):
        """Initialize the data object."""
        self._path = path   # Need to check its a valid path
        self._size = None
        self._name = path.split("/")[-1]
        self._attributes = {'Path': path}
        self._unit_of_measurement = 'MB'
        self.update()

    def update(self):
        """Get the size of the file."""
        self._size = self.get_file_size(self._path)

    def get_file_size(self, path):
        statinfo = os.stat(path)
        decimals = 2
        file_size = round(statinfo.st_size/1e6, decimals)
        return file_size

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._size

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self.ICON

    @property
    def device_state_attributes(self):
        """Attributes."""
        return self._attributes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return self._unit_of_measurement
