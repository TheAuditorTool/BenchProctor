# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest68645(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
