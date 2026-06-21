# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest81131(request: Request):
    path_value = request.path_params.get('id', '')
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
