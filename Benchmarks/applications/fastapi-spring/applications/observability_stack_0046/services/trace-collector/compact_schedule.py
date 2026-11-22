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


@router.post("/compact_schedule/{id}")
async def compact_schedule(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    gauge = RequestPayload(paragraph).value
    parsed = yaml.safe_load(gauge)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
