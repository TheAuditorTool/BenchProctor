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


@router.post("/normalize_invoice/{id}")
async def normalize_invoice(request: Request, id: str):
    caption = request.path_params.get('id', '')
    remittance = RequestPayload(caption).value
    parsed = yaml.safe_load(remittance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
