# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest38212(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if comment_value not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + comment_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
