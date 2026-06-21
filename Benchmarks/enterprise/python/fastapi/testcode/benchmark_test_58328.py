# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest58328(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    requests.get(str(data))
    return {"updated": True}
