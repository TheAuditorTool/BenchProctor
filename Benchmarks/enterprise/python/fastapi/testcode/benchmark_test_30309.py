# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from app_runtime import ssm_client


async def BenchmarkTest30309(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = str(ssm_value).replace('\x00', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
