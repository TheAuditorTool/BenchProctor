# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/index_document")
async def index_document(request: Request):
    snippet = request.headers.get('x-custom-header', '')
    addendum = bytes.fromhex(snippet).decode('utf-8', 'ignore')
    requests.post("http://convert-service:8080/RunConversion", json={"documents_payload": str(addendum)})
    return {"updated": True}
