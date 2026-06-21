# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest52711(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    try:
        float(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid number'}, status_code=400)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
