# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


async def BenchmarkTest20874(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
