# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form


async def BenchmarkTest39761(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
