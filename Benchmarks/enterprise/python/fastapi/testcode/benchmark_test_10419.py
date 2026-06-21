# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import defusedxml.ElementTree


async def BenchmarkTest10419(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
