# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import socket


async def BenchmarkTest71922(request: Request):
    user_id = request.query_params.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
