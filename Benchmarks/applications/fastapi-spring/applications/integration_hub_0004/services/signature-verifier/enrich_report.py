# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/enrich_report/{id}")
async def enrich_report(request: Request, id: str):
    summary = request.path_params.get('id', '')
    handshake = RequestPayload(summary).value
    parsed = yaml.safe_load(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
