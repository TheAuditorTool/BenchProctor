# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest02321(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
