# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest74480(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    subprocess.run(['echo', header_value], shell=False)
    return {"updated": True}
