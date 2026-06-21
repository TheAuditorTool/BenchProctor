# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import base64
from app_runtime import db


async def BenchmarkTest06201(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
