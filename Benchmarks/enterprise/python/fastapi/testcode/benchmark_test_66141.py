# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest66141(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return {"updated": True}
