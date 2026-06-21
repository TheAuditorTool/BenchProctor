# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest25012(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = relay_value(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
