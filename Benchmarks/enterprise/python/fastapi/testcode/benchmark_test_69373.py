# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest69373(request: Request, field: str = Form('')):
    field_value = field
    subprocess.Popen('echo ' + str(field_value), shell=True).wait()
    return {"updated": True}
