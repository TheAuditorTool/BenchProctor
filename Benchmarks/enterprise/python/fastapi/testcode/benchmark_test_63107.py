# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest63107(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
