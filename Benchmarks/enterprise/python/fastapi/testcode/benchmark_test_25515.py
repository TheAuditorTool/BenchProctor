# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest25515(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    return HTMLResponse('<script src="' + str(data) + '"></script>')
