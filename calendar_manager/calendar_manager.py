from icalendar import Calendar

from calendar_manager.condition import Condition
from calendar_manager.logger import Logger


def filter_events(cal, condition: Condition):
    """
    Function that filters all the events of a given calendar
    :param cal: calendar to be filtered
    :param condition: custom condition that needs to be checked
    :return: list of filtered elements
    """
    events = []
    for component in cal.walk():
        if component.name == 'VEVENT':
            summary = component.get('summary')
            description = component.get('description')
            location = component.get('location')
            dtstart = component.get('dtstart').dt
            dtend = component.get('dtend').dt
            exdate = component.get('exdate')
            latest_element = events[len(events) - 1] if len(events) > 0 else None
            if (latest_element is None
                or (latest_element.get('dtstart').dt != dtstart
                    and latest_element.get('dtend').dt != dtend)) \
                    and condition.check_location(location) \
                    and condition.check_dtends(dtend) \
                    and condition.check_descriptions(description) \
                    and condition.check_dtstarts(dtstart) \
                    and condition.check_exdates(exdate) \
                    and condition.check_summaries(summary):
                events.append(component)
    return events


def files_to_calendar(file_list):
    """
    Function that open multiple files and returns the list of opened files and the list of calendar created
    :param file_list: list of .ics input files that contains all the events
    :return: list of created calendars, list of opened files
    """
    c_list = []
    f_list = []
    for f in file_list:
        f_list.append(open(f, 'rb'))
        c_list.append(Calendar.from_ical(f_list[len(f_list) - 1].read()))
    return c_list, f_list


def create_ics_file(event_list, file_name, logger=Logger(False)):
    """
    Function that creates the output files that contains all the filtered events
    :param event_list: list of events to be printed on the file
    :param file_name: output file name
    :param logger: object that is useful to print debugging info
    """
    f = open(file_name, 'wb')
    cal = Calendar()
    for event in event_list:
        cal.add_component(event)
    f.write(cal.to_ical())
    f.close()
    logger.log('ICS file created.\t')
