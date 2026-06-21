# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22442(request: Request):
    path_value = request.path_params.get('id', '')
    processed = 'true' if str(path_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
