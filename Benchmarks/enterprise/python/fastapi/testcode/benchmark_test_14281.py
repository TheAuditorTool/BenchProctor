# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import subprocess


async def BenchmarkTest14281(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
