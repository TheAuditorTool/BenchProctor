# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest19570(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
