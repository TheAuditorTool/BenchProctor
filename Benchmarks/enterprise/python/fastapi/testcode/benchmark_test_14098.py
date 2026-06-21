# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest14098(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
