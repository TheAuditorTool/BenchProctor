# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest07646(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    if str(data).startswith('https://admin.internal/'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
