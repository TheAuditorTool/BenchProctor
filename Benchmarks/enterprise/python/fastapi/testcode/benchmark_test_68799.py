# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest68799(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    subprocess.run([str(multipart_value), '--status'], shell=False)
    return {"updated": True}
