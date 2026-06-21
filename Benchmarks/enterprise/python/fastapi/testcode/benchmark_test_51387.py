# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def ensure_str(value):
    return str(value)

async def BenchmarkTest51387(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
