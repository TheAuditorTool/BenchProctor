# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach


async def BenchmarkTest00798(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
