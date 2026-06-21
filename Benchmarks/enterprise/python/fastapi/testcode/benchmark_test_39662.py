# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest39662(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
