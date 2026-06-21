# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64


async def BenchmarkTest32305(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    os.system('echo ' + str(data))
    return {"updated": True}
