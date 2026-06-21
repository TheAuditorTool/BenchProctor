# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest70697(request: Request):
    secret_value = 'app_display_name'
    data = FormData(payload=secret_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
