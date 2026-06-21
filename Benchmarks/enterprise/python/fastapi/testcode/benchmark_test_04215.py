# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest04215(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
