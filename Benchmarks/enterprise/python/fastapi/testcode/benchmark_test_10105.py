# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest10105(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
