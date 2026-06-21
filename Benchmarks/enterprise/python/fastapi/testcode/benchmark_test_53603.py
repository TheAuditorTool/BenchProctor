# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


async def BenchmarkTest53603(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(prop_value).encode())
    return {"updated": True}
