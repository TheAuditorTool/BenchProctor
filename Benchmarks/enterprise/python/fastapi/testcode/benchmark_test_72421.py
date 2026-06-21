# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest72421(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
