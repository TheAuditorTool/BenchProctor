# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json
import os


async def BenchmarkTest57355(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
