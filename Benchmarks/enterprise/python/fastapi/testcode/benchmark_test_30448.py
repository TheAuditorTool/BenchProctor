# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import db


async def BenchmarkTest30448(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
