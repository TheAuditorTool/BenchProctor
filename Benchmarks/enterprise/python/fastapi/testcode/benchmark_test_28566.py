# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest28566(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
