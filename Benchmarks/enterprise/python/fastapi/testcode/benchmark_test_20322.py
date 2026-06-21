# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest20322(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
