from django.utils import dateformat, timezone

from records import utils as record_utils

PEOPLE_LIST_COLUMNS = ["#", "Username", "Full name", "Age category", "Actions"]


def format_datetime(dt, fmt="j M Y, g:i a"):
    local_dt = timezone.localtime(dt)
    return dateformat.format(local_dt, fmt)


def format_people_list(people):
    results = {}
    for i, person in enumerate(people):
        results[str(i + 1)] = [
            person.username,
            person.full_name,
            person.age_category,
            "add temp",
        ]
    return results


def format_temperature_records(temperature_records):
    results = {}
    for i, record in enumerate(temperature_records):
        results[str(i + 1)] = [
            record.person.username,
            record_utils.format_temperature(record.body_temperature),
            format_datetime(record.created_at),
        ]
    return results
