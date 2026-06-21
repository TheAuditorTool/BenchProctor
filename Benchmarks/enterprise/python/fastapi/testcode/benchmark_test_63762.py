# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import json


async def BenchmarkTest63762(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
