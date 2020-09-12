import json

from calendarmanager import logger


def json_parser(file_name):
    """
    Function that converts a text file into a Python dictionary.
    :param file_name: path and file name of the input JSON file.
    :return: Python dictionary of the converted JSON file.
    """
    str_help = ''
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            str_help = str_help + line.strip()
        f.close()
    except FileNotFoundError:
        logger.global_logger.log_error(f'File {file_name} not found. Change the name of the file in settings.json.')
    return json.loads(str_help)


def event_printer(events):
    """
    Function that prints on the terminal all the given events
    :param events: list of events that need to be printed
    """
    for event in events:
        logger.global_logger.log_default(
            f"{event.get('dtstart').dt.strftime('%D %H:%M UTC')}-{event.get('dtend').dt.strftime('%D %H:%M UTC')} "
            f"{event.get('summary')}: {event.get('description')} - {event.get('location')}")
