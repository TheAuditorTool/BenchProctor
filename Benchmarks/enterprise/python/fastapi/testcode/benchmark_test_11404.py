# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from fastapi import Form
import os
from types import SimpleNamespace


async def BenchmarkTest11404(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return {"updated": True}
