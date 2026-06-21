# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest32627(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    async def _evasion_task():
        os.system('echo ' + str(data))
    await _evasion_task()
    return {"updated": True}
