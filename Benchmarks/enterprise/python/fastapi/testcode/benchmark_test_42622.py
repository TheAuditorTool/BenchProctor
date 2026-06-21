# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest42622(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
