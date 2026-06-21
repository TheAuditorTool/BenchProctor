# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest67554(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
