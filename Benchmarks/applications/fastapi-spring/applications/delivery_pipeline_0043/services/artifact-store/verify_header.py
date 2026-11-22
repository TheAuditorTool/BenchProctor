# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/verify_header")
async def verify_header(request: Request):
    remark = getattr((await request.form()).get('upload'), 'filename', '')
    def normalize(value):
        return value.strip()
    note = normalize(remark)
    requests.get(str(note))
    return {"updated": True}
