# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml
import os


async def BenchmarkTest02412(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = (lambda v: v.strip())(dotenv_value)
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
