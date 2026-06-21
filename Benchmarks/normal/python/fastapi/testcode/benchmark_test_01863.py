# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest01863(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
