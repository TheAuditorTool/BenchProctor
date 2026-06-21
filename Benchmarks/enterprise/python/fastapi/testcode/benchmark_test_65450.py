# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


async def BenchmarkTest65450(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
