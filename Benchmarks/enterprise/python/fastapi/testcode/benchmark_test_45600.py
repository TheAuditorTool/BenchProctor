# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest45600(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
