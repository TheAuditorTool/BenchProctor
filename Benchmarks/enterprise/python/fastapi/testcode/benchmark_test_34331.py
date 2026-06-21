# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest34331(request: Request):
    upload_name = (await request.form()).get('upload', '')
    return HTMLResponse('<script src="' + str(upload_name) + '"></script>')
