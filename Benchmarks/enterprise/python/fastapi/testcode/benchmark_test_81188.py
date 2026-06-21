# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def to_text(value):
    return str(value).strip()

async def BenchmarkTest81188(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
