# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest57046(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
