# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


def relay_value(value):
    return value

async def BenchmarkTest09850(request: Request):
    secret_value = 'app_display_name'
    data = relay_value(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
