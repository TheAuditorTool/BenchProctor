# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest47963(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
