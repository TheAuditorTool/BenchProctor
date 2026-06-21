# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def ensure_str(value):
    return str(value)

async def BenchmarkTest06747(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ensure_str(ua_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
