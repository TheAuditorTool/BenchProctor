# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import db


async def BenchmarkTest49231(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
