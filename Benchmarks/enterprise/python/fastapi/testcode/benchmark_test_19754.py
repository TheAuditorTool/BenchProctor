# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest19754(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
