# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from fastapi import Form


async def BenchmarkTest04076(request: Request, field: str = Form('')):
    field_value = field
    subprocess.run(['echo', field_value], shell=False)
    return {"updated": True}
