# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest58660(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
