# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78979(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
