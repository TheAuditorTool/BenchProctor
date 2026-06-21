# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest00143(request: Request, field: str = Form('')):
    field_value = field
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(field_value),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
