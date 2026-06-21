# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from dataclasses import dataclass
from fastapi import Form
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest23009(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return {"updated": True}
