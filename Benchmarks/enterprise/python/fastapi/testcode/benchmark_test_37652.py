# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest37652(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parsed = urlparse(comment_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = comment_value
    return HTMLResponse('<script src="' + str(target_url) + '"></script>')
