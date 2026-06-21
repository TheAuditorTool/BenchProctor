# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest44679(request: Request):
    referer_value = request.headers.get('referer', '')
    return HTMLResponse('<script src="' + str(referer_value) + '"></script>')
