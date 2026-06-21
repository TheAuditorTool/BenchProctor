# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest56790(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = config_value if config_value else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
