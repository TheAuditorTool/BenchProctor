# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest64014(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
