# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest77533(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
