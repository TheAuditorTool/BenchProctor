# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest08183(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
