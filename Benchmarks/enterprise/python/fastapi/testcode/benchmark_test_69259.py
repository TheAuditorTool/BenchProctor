# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest69259(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    return RedirectResponse(url=str(data))
