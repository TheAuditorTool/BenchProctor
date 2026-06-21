# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest24513(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
