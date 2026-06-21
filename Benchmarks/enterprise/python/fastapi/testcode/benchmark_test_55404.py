# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import base64


async def BenchmarkTest55404(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
