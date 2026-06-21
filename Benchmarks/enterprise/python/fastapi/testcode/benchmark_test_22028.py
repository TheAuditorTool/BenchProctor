# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22028(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data, _sep, _rest = str(config_value).partition('\x00')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
