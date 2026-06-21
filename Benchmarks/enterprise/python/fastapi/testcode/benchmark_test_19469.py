# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import base64
from app_runtime import db


async def BenchmarkTest19469(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return {"updated": True}
