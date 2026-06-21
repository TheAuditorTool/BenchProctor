# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest06647(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
