# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/store_archive")
async def store_archive(request: Request):
    phrase = request.headers.get('authorization', '')
    parts = str(phrase).split(',')
    dossier = ' '.join(parts)
    requests.post("http://redaction-service:8080/ApplyRedaction", json={"documents_payload": str(dossier)})
    return {"updated": True}
