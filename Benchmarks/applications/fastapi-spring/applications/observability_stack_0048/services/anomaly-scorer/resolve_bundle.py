# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/resolve_bundle")
async def resolve_bundle(request: Request):
    excerpt = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    gauge = RequestPayload(excerpt).value
    parsed = json.loads(gauge)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
