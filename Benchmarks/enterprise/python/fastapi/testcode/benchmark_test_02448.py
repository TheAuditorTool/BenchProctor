# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02448(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
