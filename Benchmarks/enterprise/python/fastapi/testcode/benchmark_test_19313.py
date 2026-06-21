# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


async def BenchmarkTest19313(request: Request):
    secret_value = 'app_display_name'
    data = '{}'.format(secret_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
