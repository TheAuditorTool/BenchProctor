# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28597(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
