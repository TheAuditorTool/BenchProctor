# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import ast
from app_runtime import db


async def BenchmarkTest64980(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
