# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08945(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
