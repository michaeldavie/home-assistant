"""Constants for Environment Canada integration."""

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY
)

DOMAIN = "environment_canada"
ATTRIBUTION = "Data provided by Environment Canada"

# Icon codes from http://dd.weatheroffice.ec.gc.ca/citypage_weather/
# docs/current_conditions_icon_code_descriptions_e.csv
ICON_CONDITION_MAP = {
    ATTR_CONDITION_SUNNY: [0, 1],
    ATTR_CONDITION_CLEAR_NIGHT: [30, 31],
    ATTR_CONDITION_PARTLYCLOUDY: [2, 3, 4, 5, 22, 32, 33, 34, 35],
    ATTR_CONDITION_CLOUDY: [10],
    ATTR_CONDITION_RAINY: [6, 9, 11, 12, 28, 36],
    ATTR_CONDITION_LIGHTNING_RAINY: [19, 39, 46, 47],
    ATTR_CONDITION_POURING: [13],
    ATTR_CONDITION_SNOWY_RAINY: [7, 14, 15, 27, 37],
    ATTR_CONDITION_SNOWY: [8, 16, 17, 18, 25, 26, 38, 40],
    ATTR_CONDITION_WINDY: [43],
    ATTR_CONDITION_FOG: [20, 21, 23, 24, 44],
    ATTR_CONDITION_HAIL: [26, 27],
}

