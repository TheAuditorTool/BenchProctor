# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest52254(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    requests.get(str(data))
    return {"updated": True}
