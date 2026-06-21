# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest73435(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
