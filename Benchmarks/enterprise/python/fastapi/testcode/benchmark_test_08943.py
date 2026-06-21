# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest08943(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
