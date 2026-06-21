# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form


async def BenchmarkTest44788(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
