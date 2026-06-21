# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest71160(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
