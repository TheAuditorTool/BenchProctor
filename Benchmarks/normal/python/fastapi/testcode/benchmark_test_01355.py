# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest01355(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    os.remove(str(data))
    return {"updated": True}
