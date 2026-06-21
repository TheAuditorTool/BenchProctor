# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import db


async def BenchmarkTest36547(request: Request):
    secret_value = 'feature_flag_value'
    data, _sep, _rest = str(secret_value).partition('\x00')
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return {"updated": True}
