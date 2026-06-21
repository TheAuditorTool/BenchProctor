# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import subprocess


async def BenchmarkTest74533(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
