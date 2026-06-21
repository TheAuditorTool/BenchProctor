# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json
from app_runtime import db


async def BenchmarkTest09631(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
