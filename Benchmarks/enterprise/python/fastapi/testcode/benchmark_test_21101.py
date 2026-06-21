# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest21101(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
