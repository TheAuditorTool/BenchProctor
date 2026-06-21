# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21934(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
