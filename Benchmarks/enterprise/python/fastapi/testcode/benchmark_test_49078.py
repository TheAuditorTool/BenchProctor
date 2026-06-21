# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest49078(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
