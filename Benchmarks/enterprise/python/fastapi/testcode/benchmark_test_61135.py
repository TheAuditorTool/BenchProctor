# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import urllib.request


async def BenchmarkTest61135(request: Request, field: str = Form('')):
    field_value = field
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(field_value)).read()
    return {"updated": True}
