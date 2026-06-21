# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import base64


async def BenchmarkTest04510(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
