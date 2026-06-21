# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def ensure_str(value):
    return str(value)

async def BenchmarkTest05103(request: Request):
    stdin_value = input('input: ')
    data = ensure_str(stdin_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
