# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from fastapi import Form
import json


async def BenchmarkTest44885(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
