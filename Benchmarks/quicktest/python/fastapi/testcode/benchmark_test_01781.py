# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from fastapi import Form
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest01781(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
