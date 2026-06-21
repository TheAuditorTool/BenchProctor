# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest06521(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    os.chmod('/var/app/data/' + str(env_value), 0o777)
    return {"updated": True}
