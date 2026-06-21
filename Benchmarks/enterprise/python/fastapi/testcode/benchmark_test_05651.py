# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05651(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return {"updated": True}
