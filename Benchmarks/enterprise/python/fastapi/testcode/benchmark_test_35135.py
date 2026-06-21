# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest35135(request: Request):
    upload_name = (await request.form()).get('upload', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(upload_name),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
