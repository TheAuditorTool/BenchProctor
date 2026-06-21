# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def ensure_str(value):
    return str(value)

async def BenchmarkTest52665(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
