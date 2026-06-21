# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest17157(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
