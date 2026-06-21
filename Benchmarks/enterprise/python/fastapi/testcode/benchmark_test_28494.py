# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest28494(request: Request):
    upload_name = (await request.form()).get('upload', '')
    subprocess.run([str(upload_name), '--status'], shell=False)
    return {"updated": True}
