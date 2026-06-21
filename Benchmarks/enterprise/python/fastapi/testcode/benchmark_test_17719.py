# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import json


async def BenchmarkTest17719(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    return RedirectResponse(url=str(data))
