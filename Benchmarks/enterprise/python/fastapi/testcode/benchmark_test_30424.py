# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest30424(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
