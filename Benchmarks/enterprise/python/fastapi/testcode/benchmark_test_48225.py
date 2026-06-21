# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import pickle


async def BenchmarkTest48225(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
