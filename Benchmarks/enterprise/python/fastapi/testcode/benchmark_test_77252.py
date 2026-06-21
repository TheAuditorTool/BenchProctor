# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest77252(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    request.session['data'] = str(data)
    return {"updated": True}
