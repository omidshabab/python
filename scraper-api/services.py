from typing import Dict
import json as _json

def get_all_events() -> Dict:
    with open("src/events.json") as events_file:
        data =  _json.load(events_file)
        
    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "this"
    