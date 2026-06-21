# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest06617(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    with open('/var/app/data/' + str(db_value), 'r') as fh:
        content = fh.read()
    return content
