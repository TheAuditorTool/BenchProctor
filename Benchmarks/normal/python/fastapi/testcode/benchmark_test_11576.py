# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest11576(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
