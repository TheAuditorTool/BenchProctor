# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest01827(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    random.seed(int(comment_value) if str(comment_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
