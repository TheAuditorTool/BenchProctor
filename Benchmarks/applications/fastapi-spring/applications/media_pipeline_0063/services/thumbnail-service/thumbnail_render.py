# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/render_thumbnail")
async def render_thumbnail(request: Request):
    snippet = (await request.body()).decode('utf-8')
    montage = f'{snippet!s}'
    requests.post("http://caption-service:8080/ExtractCaption", json={"media_payload": str(montage)})
    return {"updated": True}
