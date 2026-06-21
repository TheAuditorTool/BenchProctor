# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest55678(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(multipart_value).encode())
    return {"updated": True}
