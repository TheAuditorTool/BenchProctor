# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01796(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
