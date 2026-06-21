# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass
import time


@dataclass
class FormData:
    payload: str

async def BenchmarkTest70229(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    store_cred = os.environ.get('APP_SECRET', '')
    key_expires_at = 4102444800
    active_key = store_cred if key_expires_at > int(time.time()) else os.environ['DATA_ENC_KEY_CURRENT']
    Fernet(active_key.encode()).encrypt(str(data).encode())
    return {"updated": True}
