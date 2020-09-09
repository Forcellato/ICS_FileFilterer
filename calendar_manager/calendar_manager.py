from icalendar import Calendar

from calendar_manager.condition import Condition
from calendar_manager.logger import Logger


def filter_events(cal, condition: Condition):
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
    c_list = []
    f_list = []
    for f in file_list:
        f_list.append(open(f, 'rb'))
        c_list.append(Calendar.from_ical(f_list[len(f_list) - 1].read()))
    return c_list, f_list


def create_ics_file(event_list, file_name, logger=Logger(False)):
    f = open(file_name, 'wb')
    cal = Calendar()
    for event in event_list:
        cal.add_component(event)
    f.write(cal.to_ical())
    f.close()
    logger.log('ICS file created.\t')
