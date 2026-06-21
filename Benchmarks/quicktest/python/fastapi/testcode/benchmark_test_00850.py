# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form


async def BenchmarkTest00850(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
