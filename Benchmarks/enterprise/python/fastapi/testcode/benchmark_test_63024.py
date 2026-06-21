# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest63024(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
