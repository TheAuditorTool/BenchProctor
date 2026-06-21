# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest11606(request: Request):
    secret_value = 'config_secret_test_abc123'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
