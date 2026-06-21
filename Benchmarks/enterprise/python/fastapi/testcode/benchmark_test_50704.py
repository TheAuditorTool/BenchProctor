# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form


async def BenchmarkTest50704(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
