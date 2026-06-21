# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest53709(request: Request):
    secret_value = 'default_setting_value'
    data = ensure_str(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return {"updated": True}
