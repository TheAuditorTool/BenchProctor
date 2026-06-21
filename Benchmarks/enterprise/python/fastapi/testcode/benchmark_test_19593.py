# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest19593(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
