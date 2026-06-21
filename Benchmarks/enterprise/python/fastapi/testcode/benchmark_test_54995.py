# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest54995(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
