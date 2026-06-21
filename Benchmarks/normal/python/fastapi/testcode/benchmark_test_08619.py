# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest08619(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
