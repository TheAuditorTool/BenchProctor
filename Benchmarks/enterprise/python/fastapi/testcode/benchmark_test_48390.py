# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48390(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    os.system('echo ' + str(data))
    return {"updated": True}
