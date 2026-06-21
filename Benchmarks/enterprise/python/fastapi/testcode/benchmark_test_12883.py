# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest12883(request: Request, field: str = Form('')):
    field_value = field
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(field_value),))
    return JSONResponse({'record': str(record)}, status_code=200)
