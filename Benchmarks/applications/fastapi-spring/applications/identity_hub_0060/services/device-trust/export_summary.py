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


@router.post("/export_summary/{id}")
async def export_summary(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    persona = RequestPayload(paragraph).value
    parsed = yaml.safe_load(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
