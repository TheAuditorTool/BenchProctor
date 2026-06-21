# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import urllib.request
import urllib.parse
import ssl


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest72284(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
