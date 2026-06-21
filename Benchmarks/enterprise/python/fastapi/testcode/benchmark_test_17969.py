# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest17969(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    os.system('echo ' + str(data))
    return {"updated": True}
