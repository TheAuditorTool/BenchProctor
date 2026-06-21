# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest00101(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    os.remove(str(data))
    return {"updated": True}
