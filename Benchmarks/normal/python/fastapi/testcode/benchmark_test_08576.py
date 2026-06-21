# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def to_text(value):
    return str(value).strip()

async def BenchmarkTest08576(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
