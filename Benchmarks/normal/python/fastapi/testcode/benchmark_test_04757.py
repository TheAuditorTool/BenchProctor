# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest04757(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    return HTMLResponse('<img src="' + str(data) + '">')
