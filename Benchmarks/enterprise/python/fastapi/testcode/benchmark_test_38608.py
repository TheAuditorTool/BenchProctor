# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest38608(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    subprocess.run([str(cookie_value), '--status'], shell=False)
    return {"updated": True}
