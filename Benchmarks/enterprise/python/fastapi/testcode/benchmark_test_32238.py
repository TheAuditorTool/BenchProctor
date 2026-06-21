# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32238(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
