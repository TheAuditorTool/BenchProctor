# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
from app_runtime import db


async def BenchmarkTest17782(request: Request, field: str = Form('')):
    field_value = field
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(field_value),))
    logging.info('request processed')
    return {"updated": True}
