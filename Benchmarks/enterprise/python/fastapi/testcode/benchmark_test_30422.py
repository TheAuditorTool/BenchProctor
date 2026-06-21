# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest30422(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    return HTMLResponse('<script src="' + str(xml_value) + '"></script>')
