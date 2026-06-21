# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace


async def BenchmarkTest65313(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
