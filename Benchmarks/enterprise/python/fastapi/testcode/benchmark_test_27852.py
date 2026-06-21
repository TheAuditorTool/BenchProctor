# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import pickle


async def BenchmarkTest27852(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
