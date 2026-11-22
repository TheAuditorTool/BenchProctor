# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/run_conversion")
async def run_conversion(request: Request):
    citation = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    requests.post("http://index-builder:8080/IndexDocument", json={"documents_payload": str(dossier)})
    return {"updated": True}
