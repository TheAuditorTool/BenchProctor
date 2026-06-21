# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest79373(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return HTMLResponse('<img src="' + str(upload_name) + '">')
