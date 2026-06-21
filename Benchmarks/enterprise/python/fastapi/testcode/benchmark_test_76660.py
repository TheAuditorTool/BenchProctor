# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76660(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
