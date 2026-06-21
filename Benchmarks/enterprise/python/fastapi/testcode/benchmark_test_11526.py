# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest11526(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
