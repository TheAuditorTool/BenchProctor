# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest04506(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    pending = list(str(config_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
