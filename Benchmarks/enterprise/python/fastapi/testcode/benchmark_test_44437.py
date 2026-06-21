# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest44437(request: Request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    kind = 'json' if str(yaml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = yaml_value
            data = parsed
        case _:
            data = yaml_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
