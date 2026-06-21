# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest12029(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
