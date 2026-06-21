# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


async def BenchmarkTest35968(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
