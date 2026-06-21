# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest03431(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
