# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest39840(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
