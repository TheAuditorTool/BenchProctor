# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest38815(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
