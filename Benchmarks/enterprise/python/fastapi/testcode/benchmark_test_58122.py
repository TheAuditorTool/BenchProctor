# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest58122(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
