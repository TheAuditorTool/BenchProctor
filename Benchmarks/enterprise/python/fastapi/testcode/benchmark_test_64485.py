# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


async def BenchmarkTest64485(request: Request, field: str = Form('')):
    field_value = field
    requests.get('https://api.pycdn.io/data', params={'q': str(field_value)}, verify=False)
    return {"updated": True}
