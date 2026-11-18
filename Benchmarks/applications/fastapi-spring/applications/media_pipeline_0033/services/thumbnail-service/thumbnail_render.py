# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/render_thumbnail")
async def render_thumbnail(request: Request):
    transcript = request.headers.get('x-custom-header', '')
    rendition = bytes.fromhex(transcript).decode('utf-8', 'ignore')
    requests.post("http://upload-gateway:8080/UploadAsset", json={"media_payload": str(rendition)})
    return {"updated": True}
