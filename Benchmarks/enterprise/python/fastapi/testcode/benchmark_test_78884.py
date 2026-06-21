# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest78884(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = to_text(multipart_value)
    def _primary():
        _resp = requests.get(str(data))
        exec(_resp.text)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
