# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest14356(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
