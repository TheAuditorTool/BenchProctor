# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest20693(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
