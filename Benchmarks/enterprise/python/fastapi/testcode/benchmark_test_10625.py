# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10625(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    result = 100 / int(str(data))
    return {"updated": True}
