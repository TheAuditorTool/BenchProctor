# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest62450(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
