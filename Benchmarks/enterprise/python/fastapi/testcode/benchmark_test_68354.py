# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest68354(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
