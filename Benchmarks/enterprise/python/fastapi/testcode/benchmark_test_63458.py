# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse


async def BenchmarkTest63458(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parsed = urlparse(multipart_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = multipart_value
    requests.get(str(target_url))
    return {"updated": True}
