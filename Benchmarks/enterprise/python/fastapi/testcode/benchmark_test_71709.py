# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
import subprocess


async def BenchmarkTest71709(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
