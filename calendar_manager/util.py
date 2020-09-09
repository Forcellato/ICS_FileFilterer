import json

from calendar_manager.logger import Logger


def json_parser(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    strhelp = ''
    for line in lines:
        strhelp = strhelp + line.strip()
    f.close()
    return json.loads(strhelp)


def event_printer(events):
    for event in events:
        print(f"{event.get('dtstart').dt.strftime('%D %H:%M UTC')}-{event.get('dtend').dt.strftime('%D %H:%M UTC')} "
              f"{event.get('summary')}: {event.get('description')} - {event.get('location')}")
