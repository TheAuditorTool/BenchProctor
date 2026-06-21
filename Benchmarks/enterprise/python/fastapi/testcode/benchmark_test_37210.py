# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import json
import defusedxml.ElementTree


async def BenchmarkTest37210(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
