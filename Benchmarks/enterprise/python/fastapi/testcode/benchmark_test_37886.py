# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest37886(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return RedirectResponse(url=str(data))
