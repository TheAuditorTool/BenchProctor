# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest41032(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
