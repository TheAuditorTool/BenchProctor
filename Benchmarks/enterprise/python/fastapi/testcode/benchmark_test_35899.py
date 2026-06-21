# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from types import SimpleNamespace


async def BenchmarkTest35899(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
