# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import socket
from app_runtime import db


async def BenchmarkTest78775(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
