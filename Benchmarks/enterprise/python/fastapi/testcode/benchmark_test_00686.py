# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest00686(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
