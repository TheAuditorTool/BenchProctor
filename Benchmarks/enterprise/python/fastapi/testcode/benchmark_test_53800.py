# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest53800(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return HTMLResponse('<div>' + str(data) + '</div>')
