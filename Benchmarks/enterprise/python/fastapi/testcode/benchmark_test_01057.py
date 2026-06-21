# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from fastapi import Form


async def BenchmarkTest01057(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
