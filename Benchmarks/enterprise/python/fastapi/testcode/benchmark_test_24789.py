# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest24789(request: Request):
    origin_value = request.headers.get('origin', '')
    return HTMLResponse('<script src="' + str(origin_value) + '"></script>')
