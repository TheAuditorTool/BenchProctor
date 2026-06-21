# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest01567(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
