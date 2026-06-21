# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


async def BenchmarkTest62643(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
