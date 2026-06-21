# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest27693(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    return HTMLResponse('<script src="' + str(multipart_value) + '"></script>')
