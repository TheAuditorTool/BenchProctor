# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest19089(request: Request, field: str = Form('')):
    field_value = field
    _resp = requests.get(str(field_value))
    exec(_resp.text)
    return {"updated": True}
