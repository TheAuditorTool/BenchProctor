# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form
import time


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest37699(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
