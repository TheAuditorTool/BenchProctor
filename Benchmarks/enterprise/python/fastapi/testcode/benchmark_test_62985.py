# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest62985(request: Request):
    upload_name = (await request.form()).get('upload', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.seteuid(65534)
    return {"updated": True}
