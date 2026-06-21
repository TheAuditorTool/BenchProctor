# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest68996(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(raw_body),))
    return JSONResponse({'record': str(record)}, status_code=200)
