# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/build_manifest")
async def build_manifest(request: Request):
    synopsis = getattr((await request.form()).get('upload'), 'filename', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(synopsis)
    requests.post("http://upload-gateway:8080/UploadAsset", json={"media_payload": str(rendition)})
    return {"updated": True}
