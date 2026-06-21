# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest00997(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    return HTMLResponse('<script src="' + str(data) + '"></script>')
