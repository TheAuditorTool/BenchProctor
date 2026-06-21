# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json


async def BenchmarkTest55804(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
