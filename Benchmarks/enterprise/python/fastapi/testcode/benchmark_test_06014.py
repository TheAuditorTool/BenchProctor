# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest06014(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
