# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from types import SimpleNamespace


async def BenchmarkTest79551(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
