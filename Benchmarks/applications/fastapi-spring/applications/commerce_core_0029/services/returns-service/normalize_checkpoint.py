# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/normalize_checkpoint")
async def normalize_checkpoint(request: Request):
    notice = (await request.form()).get('multipart_field', '')
    backorder = RequestPayload(notice).value
    pickle.loads(base64.b64decode(backorder))
    return {"updated": True}
