# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest03814(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
