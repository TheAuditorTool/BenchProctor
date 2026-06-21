# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import auth_check


async def BenchmarkTest24609(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    auth_check('user', data)
    return {"updated": True}
