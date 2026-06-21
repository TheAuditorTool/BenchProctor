# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest18278(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parsed = urlparse(upload_name)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = upload_name
    requests.get(str(target_url))
    return {"updated": True}
