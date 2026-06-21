# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest08400(request: Request):
    ua_value = request.headers.get('user-agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
