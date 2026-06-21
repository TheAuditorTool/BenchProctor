# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from app_runtime import ssm_client


async def BenchmarkTest62004(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    def normalize(value):
        return value.strip()
    data = normalize(ssm_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
