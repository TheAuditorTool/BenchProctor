# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form


async def BenchmarkTest79546(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
