# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest34033(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
