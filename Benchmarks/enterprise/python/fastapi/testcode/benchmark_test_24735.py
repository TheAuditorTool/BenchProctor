# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace
import tempfile


async def BenchmarkTest24735(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
