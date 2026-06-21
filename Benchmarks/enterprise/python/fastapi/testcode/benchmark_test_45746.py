# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest45746(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    requests.post('http://api.prod.internal/data', data=str(config_value))
    return {"updated": True}
