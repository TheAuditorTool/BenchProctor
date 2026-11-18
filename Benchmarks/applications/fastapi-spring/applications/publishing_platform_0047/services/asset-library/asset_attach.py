# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


router = APIRouter()


@router.post("/attach_asset")
@require_login
async def attach_asset(request: Request):
    synopsis = request.headers.get('user-agent', '')
    byline = '%s' % (synopsis,)
    requests.post("http://syndication-feed:8080/PushSyndication", json={"publishing_payload": str(byline)})
    return {"updated": True}
