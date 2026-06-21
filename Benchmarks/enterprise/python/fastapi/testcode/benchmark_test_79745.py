# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79745(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
