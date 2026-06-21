# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32973(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/uploads/' + str(env_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
