# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import subprocess


async def BenchmarkTest03718(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
