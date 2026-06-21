# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest38904(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
