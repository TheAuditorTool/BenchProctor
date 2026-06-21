# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest51100(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(comment_value))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
