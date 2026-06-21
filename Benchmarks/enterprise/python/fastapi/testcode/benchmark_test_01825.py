# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest01825(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
