# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest45525(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
