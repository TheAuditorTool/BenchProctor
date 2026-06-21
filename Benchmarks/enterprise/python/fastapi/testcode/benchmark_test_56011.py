# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote
from fastapi import Form
from app_runtime import db


async def BenchmarkTest56011(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
