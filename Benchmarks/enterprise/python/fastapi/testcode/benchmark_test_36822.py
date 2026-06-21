# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import urllib.request
import urllib.parse
import ssl


def normalise_input(value):
    return value.strip()

async def BenchmarkTest36822(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
