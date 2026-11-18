# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/attach_asset")
async def attach_asset(request: Request):
    summary = request.headers.get('user-agent', '')
    requests.post("http://article-api:8080/DraftArticle", json={"publishing_payload": str(summary)})
    return {"updated": True}
