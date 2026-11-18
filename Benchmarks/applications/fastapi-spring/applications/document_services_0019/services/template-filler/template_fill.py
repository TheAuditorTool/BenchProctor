# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import unquote


router = APIRouter()


@router.post("/fill_template")
async def fill_template(request: Request):
    passage = (await request.form()).get('field', '')
    dossier = unquote(passage)
    requests.post("http://redaction-service:8080/ApplyRedaction", json={"documents_payload": str(dossier)})
    return {"updated": True}
