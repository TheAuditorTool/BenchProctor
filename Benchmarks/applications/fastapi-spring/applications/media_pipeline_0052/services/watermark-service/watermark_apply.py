# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/apply_watermark")
async def apply_watermark(request: Request):
    tagline = request.headers.get('x-custom-header', '')
    rendition = bytes.fromhex(tagline).decode('utf-8', 'ignore')
    requests.post("http://metadata-index:8080/IndexMetadata", json={"media_payload": str(rendition)})
    return {"updated": True}
