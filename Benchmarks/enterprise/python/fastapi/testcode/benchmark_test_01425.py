# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest01425(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return {"updated": True}
