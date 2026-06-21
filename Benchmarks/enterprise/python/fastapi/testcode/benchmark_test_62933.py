# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest62933(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
