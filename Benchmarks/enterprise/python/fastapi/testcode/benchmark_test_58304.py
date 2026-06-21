# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest58304(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
