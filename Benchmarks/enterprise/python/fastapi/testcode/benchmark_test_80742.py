# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from fastapi import Form


async def BenchmarkTest80742(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
