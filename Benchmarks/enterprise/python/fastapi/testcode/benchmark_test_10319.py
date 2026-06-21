# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest10319(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
