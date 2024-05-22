from datetime import datetime


def kelvin_to_celsius(kelvin):
    """
    Convert kelvin value to celsius.

    :param kelvin: Kelvin value (integer or float)
    :return: Celsius value (float)
    """
    return round(kelvin - 273.15, 2)


def convert_epoch_to_timestamp(epoch_time, fmt='%Y-%m-%d %H:%M:%S'):
    """
    Convert epoch time to a formatted timestamp string.

    :param epoch_time: Epoch time (integer or float)
    :param fmt: Format for the output timestamp string
    :return: Formatted timestamp string
    """
    timestamp = datetime.fromtimestamp(epoch_time)
    return timestamp.strftime(fmt)
