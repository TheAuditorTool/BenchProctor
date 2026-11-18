# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/index_metadata")
async def index_metadata(request: Request):
    passage = request.headers.get('user-agent', '')
    montage, _sep, _rest = str(passage).partition('\x00')
    requests.post("http://thumbnail-service:8080/RenderThumbnail", json={"media_payload": str(montage)})
    return {"updated": True}
