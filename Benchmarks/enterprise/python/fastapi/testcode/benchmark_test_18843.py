# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest18843(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    return HTMLResponse('<script src="' + str(data) + '"></script>')
