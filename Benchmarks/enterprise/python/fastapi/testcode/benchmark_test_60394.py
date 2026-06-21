# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest60394(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
