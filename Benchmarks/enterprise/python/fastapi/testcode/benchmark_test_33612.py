# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest33612(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
