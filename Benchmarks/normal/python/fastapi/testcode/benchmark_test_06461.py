# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest06461(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    return HTMLResponse('<div>' + str(data) + '</div>')
