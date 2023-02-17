from typing import Iterator
import datetime as _dt

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)