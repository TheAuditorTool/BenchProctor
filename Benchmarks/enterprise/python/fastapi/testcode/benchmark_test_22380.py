# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
from app_runtime import db


async def BenchmarkTest22380(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
