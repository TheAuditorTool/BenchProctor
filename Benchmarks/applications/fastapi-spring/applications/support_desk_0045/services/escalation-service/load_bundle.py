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


@router.post("/load_bundle")
async def load_bundle(request: Request):
    remark = (await request.form()).get('multipart_field', '')
    inquiry = RequestPayload(remark).value
    pickle.loads(base64.b64decode(inquiry))
    return {"updated": True}
