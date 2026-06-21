# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest37871(request: Request):
    upload_name = (await request.form()).get('upload', '')
    processed = shlex.quote(upload_name)
    os.system('echo ' + str(processed))
    return {"updated": True}
