# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import socket


async def BenchmarkTest02511(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
