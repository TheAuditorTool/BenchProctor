# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest67280(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    processed = shlex.quote(multipart_value)
    os.system('echo ' + str(processed))
    return {"updated": True}
