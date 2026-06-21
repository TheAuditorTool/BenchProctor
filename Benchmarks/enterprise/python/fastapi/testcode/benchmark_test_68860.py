# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest68860(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    processed = 'true' if str(db_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return {"updated": True}
