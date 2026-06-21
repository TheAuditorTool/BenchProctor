# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest14329(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
