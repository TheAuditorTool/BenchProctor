# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def normalise_input(value):
    return value.strip()

async def BenchmarkTest75396(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
