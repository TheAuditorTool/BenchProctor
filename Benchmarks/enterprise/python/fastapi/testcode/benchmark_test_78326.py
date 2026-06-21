# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from types import SimpleNamespace


async def BenchmarkTest78326(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    Fernet(processed.encode() if isinstance(processed, str) else processed).encrypt(b'data')
    return {"updated": True}
