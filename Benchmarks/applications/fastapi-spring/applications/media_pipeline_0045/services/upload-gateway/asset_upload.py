# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/upload_asset")
async def upload_asset(request: Request):
    with open('/tmp/data', 'r') as fh:
        notice = fh.read()
    def normalize(value):
        return value.strip()
    rendition = normalize(notice)
    requests.post("http://transcode-service:8080/EnqueueTranscode", json={"media_payload": str(rendition)})
    return {"updated": True}
