# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest59924(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
