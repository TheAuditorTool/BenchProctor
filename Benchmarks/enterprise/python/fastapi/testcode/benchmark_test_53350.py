# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest53350(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    os.system('echo ' + str(processed))
    return {"updated": True}
