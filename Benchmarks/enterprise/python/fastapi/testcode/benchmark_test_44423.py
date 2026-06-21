# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest44423(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
