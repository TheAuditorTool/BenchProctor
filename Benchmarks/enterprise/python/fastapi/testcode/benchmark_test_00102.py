# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest00102(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
