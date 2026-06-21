# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


async def BenchmarkTest04792(request: Request):
    secret_value = 'default_setting_value'
    data, _sep, _rest = str(secret_value).partition('\x00')
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
