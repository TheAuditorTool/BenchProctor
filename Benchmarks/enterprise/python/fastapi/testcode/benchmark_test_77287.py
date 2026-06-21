# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json
from app_runtime import auth_check


async def BenchmarkTest77287(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    auth_check('user', data)
    return {"updated": True}
