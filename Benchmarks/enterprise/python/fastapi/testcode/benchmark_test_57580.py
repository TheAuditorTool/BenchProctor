# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest57580(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', comment_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = comment_value
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
