# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/cut_release")
async def cut_release(request: Request):
    footnote = request.headers.get('referer', '')
    parts = str(footnote).split(',')
    wording = ' '.join(parts)
    requests.post("http://changelog-builder:8080/BuildChangelog", json={"delivery_payload": str(wording)})
    return {"updated": True}
