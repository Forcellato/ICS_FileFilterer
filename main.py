from calendar_manager.calendar_manager import files_to_calendar, filter_events, create_ics_file
from calendar_manager.condition import create_condition
from calendar_manager.util import json_parser, event_printer
from threading import Thread
from calendar_manager.logger import Logger
from time import time

if __name__ == '__main__':
    t = time()
    settings = json_parser('settings.json')
    logger = Logger(settings['verbose'], settings['cursor'])
    logger.log('Settings parsed successfully.')
    calendar_list, icalfile_list = files_to_calendar(settings['calendar_files'])
    logger.log('Files converted into multiple calendars.')
    condition = create_condition(settings['conditions'])
    events = []
    for calendar in calendar_list:
        aux = filter_events(calendar, condition)
        events.extend(aux)
        logger.log_info(f'Event filtered. Before: {len(calendar.walk())}, after: {len(aux)}.')
    logger.log_info(f'Total events: {len(events)}.')
    for file in icalfile_list:
        file.close()
    logger.log('ICS input files closed.')
    th1 = Thread(target=event_printer, args=[events])
    th2 = Thread(target=create_ics_file, args=[events, settings['output_file'], logger])
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    logger.log(f'Exec time: {time() - t}')
