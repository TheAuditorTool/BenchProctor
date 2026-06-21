# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest05048(request: Request, field: str = Form('')):
    field_value = field
    requests.get('https://api.pycdn.io/data', params={'q': str(field_value)}, verify=True)
    return {"updated": True}
