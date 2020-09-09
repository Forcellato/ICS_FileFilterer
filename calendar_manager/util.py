import json

from calendar_manager.logger import Logger


def json_parser(file_name):
    """
    Function that converts a text file into a Python dictionary.
    :param file_name: path and file name of the input JSON file.
    :return: Python dictionary of the converted JSON file.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    strhelp = ''
    for line in lines:
        strhelp = strhelp + line.strip()
    f.close()
    return json.loads(strhelp)


def event_printer(events):
    """
    Function that prints on the terminal all the given events
    :param events: list of events that need to be printed
    """
    for event in events:
        print(f"{event.get('dtstart').dt.strftime('%D %H:%M UTC')}-{event.get('dtend').dt.strftime('%D %H:%M UTC')} "
              f"{event.get('summary')}: {event.get('description')} - {event.get('location')}")
