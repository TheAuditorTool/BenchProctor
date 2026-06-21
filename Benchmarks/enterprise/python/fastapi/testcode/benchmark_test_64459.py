# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest64459(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
