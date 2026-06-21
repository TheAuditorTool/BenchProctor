# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest18871(request: Request):
    user_id = request.query_params.get('id', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(user_id),))
    if result is None:
        return JSONResponse({'error': 'not found'}, status_code=404)
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
