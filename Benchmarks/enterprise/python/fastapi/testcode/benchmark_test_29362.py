# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest29362(request: Request):
    user_id = request.query_params.get('id', '')
    parsed = urlparse(user_id)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = user_id
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return {"updated": True}
