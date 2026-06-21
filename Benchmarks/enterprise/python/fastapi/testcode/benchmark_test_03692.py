# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import yaml


async def BenchmarkTest03692(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    kind = 'json' if str(prop_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = prop_value
            data = parsed
        case _:
            data = prop_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
