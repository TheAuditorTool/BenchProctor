# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/store_archive")
async def store_archive(request: Request):
    note = request.headers.get('user-agent', '')
    pending = list(str(note).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    addendum = ','.join(collected)
    requests.post("http://ocr-service:8080/ExtractText", json={"documents_payload": str(addendum)})
    return {"updated": True}
