# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import redis_client


router = APIRouter()


@router.post("/attach_asset")
async def attach_asset(request: Request):
    heading = redis_client.get('user_data')
    kind = 'json' if str(heading).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            addendum = str(heading).strip()
        case _:
            addendum = str(heading)
    requests.post("http://preview-renderer:8080/RenderPreview", json={"publishing_payload": str(addendum)})
    return {"updated": True}
