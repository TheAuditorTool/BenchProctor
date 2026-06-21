# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest01972(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
