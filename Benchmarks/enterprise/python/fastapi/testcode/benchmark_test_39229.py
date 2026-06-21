# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest39229(request: Request):
    ua_value = request.headers.get('user-agent', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(ua_value),))
    return {"updated": True}
