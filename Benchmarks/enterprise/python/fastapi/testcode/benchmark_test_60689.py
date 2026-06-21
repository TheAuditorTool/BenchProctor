# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest60689(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    os.system('echo ' + str(data))
    return {"updated": True}
