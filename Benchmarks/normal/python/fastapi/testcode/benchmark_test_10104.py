# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest10104(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
