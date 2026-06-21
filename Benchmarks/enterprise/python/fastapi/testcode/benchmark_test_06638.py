# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring
from app_runtime import ssm_client


async def BenchmarkTest06638(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data, _sep, _rest = str(ssm_value).partition('\x00')
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
