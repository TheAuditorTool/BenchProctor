# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest76574(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
