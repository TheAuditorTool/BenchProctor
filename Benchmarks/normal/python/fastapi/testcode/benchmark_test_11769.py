# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest11769(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
