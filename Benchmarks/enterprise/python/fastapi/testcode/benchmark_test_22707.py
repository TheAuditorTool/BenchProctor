# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest22707(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return HTMLResponse('<script src="' + str(data) + '"></script>')
