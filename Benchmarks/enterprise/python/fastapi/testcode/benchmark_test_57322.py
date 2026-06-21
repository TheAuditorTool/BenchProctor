# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import keyring
import ast
from app_runtime import ssm_client


async def BenchmarkTest57322(request: Request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    try:
        data = str(ast.literal_eval(ssm_value))
    except (ValueError, SyntaxError):
        data = ssm_value
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
