# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest25535(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
