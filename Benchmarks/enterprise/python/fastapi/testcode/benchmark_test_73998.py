# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest73998(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
