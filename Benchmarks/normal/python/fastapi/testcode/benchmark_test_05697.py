# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import auth_check


async def BenchmarkTest05697(request: Request):
    secret_value = 'default_config_label'
    data = f'{secret_value:.200s}'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return {"updated": True}
