from calendar_manager.calendar_manager import files_to_calendar, filter_events, create_ics_file
from calendar_manager.condition import create_condition
from calendar_manager.util import json_parser, event_printer
from threading import Thread
from calendar_manager.logger import Logger
from time import time

if __name__ == '__main__':
    t = time()  # for debugging purpose it allows to get the execution time
    settings = json_parser('settings.json')  # this parses the setting.json file into a Python dictionary
    logger = Logger(settings['verbose'], settings['cursor'])  # this create the custom logger
    logger.log('Settings parsed successfully.')
    # this converts all the input files into a calendar list and a list of opened files.
    calendar_list, ics_file_list = files_to_calendar(settings['calendar_files'])
    logger.log('Files converted into multiple calendars.')
    # this create the condition object used for filtering the input events
    condition = create_condition(settings['conditions'])
    events = []
    for calendar in calendar_list:
        aux = filter_events(calendar, condition)  # this returns the list of filtered events of the given calendar
        events.extend(aux)
        logger.log_info(f'Event filtered. Before: {len(calendar.walk())}, after: {len(aux)}.')
    logger.log_info(f'Total events: {len(events)}.')
    # the opened input files are now useless, this closes all the opened files
    for file in ics_file_list:
        file.close()
    logger.log('ICS input files closed.')
    # for optimization purpose, 2 threads are created
    th1 = Thread(target=event_printer, args=[events])  # this one print all the filtered elements on the terminal
    # this one creates the output file
    th2 = Thread(target=create_ics_file, args=[events, settings['output_file'], logger])
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    logger.log(f'Exec time: {time() - t}')
