# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import pickle


async def BenchmarkTest06083(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
