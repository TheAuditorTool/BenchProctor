# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/summarize_config")
async def summarize_config(request: Request):
    phrase = (await request.form()).get('field', '')
    pending = list(str(phrase).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    dossier = ','.join(collected)
    requests.get(str(dossier))
    return {"updated": True}
