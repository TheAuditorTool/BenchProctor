# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest62492(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = db_value
            data = parsed
        case _:
            data = db_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
