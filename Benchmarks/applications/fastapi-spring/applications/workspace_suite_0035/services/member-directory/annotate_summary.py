# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/annotate_summary")
async def annotate_summary(request: Request):
    paragraph = getattr((await request.form()).get('upload'), 'filename', '')
    def normalize(value):
        return value.strip()
    wording = normalize(paragraph)
    requests.get(str(wording))
    return {"updated": True}
