# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest11434(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    return RedirectResponse(url=str(data))
