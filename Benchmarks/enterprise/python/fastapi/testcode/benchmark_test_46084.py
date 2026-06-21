# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest46084(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    return HTMLResponse('<div>' + str(data) + '</div>')
