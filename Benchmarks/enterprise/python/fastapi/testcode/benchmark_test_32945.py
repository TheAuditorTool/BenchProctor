# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from urllib.parse import unquote


async def BenchmarkTest32945(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
