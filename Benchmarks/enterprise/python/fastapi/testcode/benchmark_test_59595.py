# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest59595(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
