# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import db


async def BenchmarkTest76912(request: Request):
    secret_value = 'app_display_name'
    if secret_value:
        data = secret_value
    else:
        data = ''
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
