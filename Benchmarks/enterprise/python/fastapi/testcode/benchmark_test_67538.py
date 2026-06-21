# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest67538(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
