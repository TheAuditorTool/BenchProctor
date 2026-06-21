# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json
import requests


async def BenchmarkTest13823(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
