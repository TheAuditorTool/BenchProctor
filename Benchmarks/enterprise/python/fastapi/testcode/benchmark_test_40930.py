# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest40930(request: Request):
    stdin_value = input('input: ')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(stdin_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
