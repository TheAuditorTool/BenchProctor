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


@router.post("/normalize_document")
async def normalize_document(request: Request):
    remark = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    synopsis = RequestPayload(remark).value
    parsed = json.loads(synopsis)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
