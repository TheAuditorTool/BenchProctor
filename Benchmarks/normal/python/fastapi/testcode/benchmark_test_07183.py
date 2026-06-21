# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest07183(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.get(str(data))
    return {"updated": True}
