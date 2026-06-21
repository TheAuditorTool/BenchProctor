# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import auth_check


async def BenchmarkTest66240(request: Request):
    secret_value = 'default_config_label'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return {"updated": True}
