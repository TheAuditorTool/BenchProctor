# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08393(request: Request):
    secret_value = 'app_display_name'
    data = FormData(payload=secret_value).payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    auth_check(str(data), store_cred)
    return {"updated": True}
