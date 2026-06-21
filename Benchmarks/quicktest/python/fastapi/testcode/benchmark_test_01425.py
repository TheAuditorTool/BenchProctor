# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01425(request: Request):
    upload_name = (await request.form()).get('upload', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['user'] = str(data)
    return {"updated": True}
