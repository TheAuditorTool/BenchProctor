# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest34158(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    os.remove(str(data))
    return {"updated": True}
