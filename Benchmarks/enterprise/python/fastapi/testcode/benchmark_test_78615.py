# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest78615(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
