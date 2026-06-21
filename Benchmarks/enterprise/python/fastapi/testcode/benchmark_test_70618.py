# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest70618(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
