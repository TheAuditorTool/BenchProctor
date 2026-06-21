# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def ensure_str(value):
    return str(value)

async def BenchmarkTest48489(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ensure_str(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
