# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest07078(request: Request, field: str = Form('')):
    field_value = field
    os.system('echo ' + str(field_value))
    return {"updated": True}
