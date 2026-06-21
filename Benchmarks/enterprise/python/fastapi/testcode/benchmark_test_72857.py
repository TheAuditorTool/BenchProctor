# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest72857(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
