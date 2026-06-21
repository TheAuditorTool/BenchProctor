# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form
import subprocess


async def BenchmarkTest72794(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
