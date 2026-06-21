# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from app_runtime import db


async def BenchmarkTest25667(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
