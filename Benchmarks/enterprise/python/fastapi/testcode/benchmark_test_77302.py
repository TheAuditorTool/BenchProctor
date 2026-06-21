# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest77302(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
