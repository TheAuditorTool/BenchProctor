# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import urllib.request


async def BenchmarkTest30433(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
