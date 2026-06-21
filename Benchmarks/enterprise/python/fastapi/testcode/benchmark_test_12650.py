# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12650(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
