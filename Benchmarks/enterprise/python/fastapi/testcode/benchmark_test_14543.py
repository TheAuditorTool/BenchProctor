# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest14543(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
