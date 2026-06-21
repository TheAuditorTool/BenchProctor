# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


async def BenchmarkTest63537(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(xml_value).encode())
    return {"updated": True}
