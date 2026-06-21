# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest78353(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '{}'.format(config_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
