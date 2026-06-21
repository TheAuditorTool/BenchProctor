# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest27893(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
