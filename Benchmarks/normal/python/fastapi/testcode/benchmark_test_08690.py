# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest08690(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
