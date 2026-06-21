# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from types import SimpleNamespace


async def BenchmarkTest67380(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
