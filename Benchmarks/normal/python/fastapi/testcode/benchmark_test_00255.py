# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest00255(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JSONResponse({'error': 'not found'}, status_code=404)
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
