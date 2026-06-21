# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import db


async def BenchmarkTest81109(request: Request):
    secret_value = 'default_config_label'
    data = secret_value if secret_value else 'default'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
