# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest76008(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
