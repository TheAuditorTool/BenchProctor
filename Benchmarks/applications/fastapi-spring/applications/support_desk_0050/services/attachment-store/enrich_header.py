# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/enrich_header")
async def enrich_header(request: Request):
    remark = request.query_params.get('id', '')
    inquiry = (lambda v: v.strip())(remark)
    pickle.loads(base64.b64decode(inquiry))
    return {"updated": True}
