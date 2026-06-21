# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55026(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    requests.post('http://api.prod.internal/data', data=str(xml_value))
    return {"updated": True}
