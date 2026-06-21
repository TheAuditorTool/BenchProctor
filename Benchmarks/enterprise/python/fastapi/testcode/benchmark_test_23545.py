# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest23545(request: Request):
    referer_value = request.headers.get('referer', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(referer_value),))
    return JSONResponse({'record': str(record)}, status_code=200)
