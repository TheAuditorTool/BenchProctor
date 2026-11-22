# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/review_editorial")
async def review_editorial(request: Request):
    synopsis = request.headers.get('referer', '')
    byline, _sep, _rest = str(synopsis).partition('\x00')
    requests.post("http://preview-renderer:8080/RenderPreview", json={"publishing_payload": str(byline)})
    return {"updated": True}
