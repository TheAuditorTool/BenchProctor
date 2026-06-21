# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest03633(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    globals()['counter'] = int(data)
    return {"updated": True}
