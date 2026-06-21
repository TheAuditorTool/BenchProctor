# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


async def BenchmarkTest07832(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not auth_check(str(comment_value), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
