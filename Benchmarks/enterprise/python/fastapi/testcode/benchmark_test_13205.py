# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from app_runtime import ssm_client


async def BenchmarkTest13205(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    kind = 'json' if str(ssm_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ssm_value
            data = parsed
        case _:
            data = ssm_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
