# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


async def BenchmarkTest64309(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not auth_check(request.session.get('user', ''), str(comment_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
