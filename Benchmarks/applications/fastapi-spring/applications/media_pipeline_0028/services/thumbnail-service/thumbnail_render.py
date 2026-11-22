# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import os


router = APIRouter()


@router.post("/render_thumbnail")
async def render_thumbnail(request: Request):
    citation = os.environ.get('MEDIA_INPUT_0028', '')
    rendition = f'{citation!s}'
    requests.post("http://metadata-index:8080/IndexMetadata", json={"media_payload": str(rendition)})
    return {"updated": True}
