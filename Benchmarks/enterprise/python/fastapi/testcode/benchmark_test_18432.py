# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest18432(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
