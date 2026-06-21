# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31188(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
