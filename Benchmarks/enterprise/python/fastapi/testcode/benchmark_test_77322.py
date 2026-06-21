# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from fastapi import Form


async def BenchmarkTest77322(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
