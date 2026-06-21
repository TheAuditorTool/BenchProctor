# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


async def BenchmarkTest52389(request: Request):
    secret_value = 'default_config_label'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(secret_value).encode())
    return {"updated": True}
