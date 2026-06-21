# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest42269(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    return HTMLResponse('<div>' + str(data) + '</div>')
