# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest65064(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
