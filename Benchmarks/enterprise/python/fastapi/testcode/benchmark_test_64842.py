# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest64842(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.system('echo ' + str(data))
    return {"updated": True}
