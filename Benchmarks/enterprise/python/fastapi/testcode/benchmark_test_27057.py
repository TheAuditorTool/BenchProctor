# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest27057(request: Request):
    upload_name = request.query_params.get('filename', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
