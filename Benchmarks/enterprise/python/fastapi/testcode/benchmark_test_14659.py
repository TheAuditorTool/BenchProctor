# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest14659(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
