# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest01336(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
