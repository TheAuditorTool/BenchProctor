# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/publish_artifact")
async def publish_artifact(request: Request):
    remark = request.headers.get('user-agent', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            note = str(remark).strip()
        case _:
            note = str(remark)
    requests.post("http://canary-controller:8080/PromoteCanary", json={"delivery_payload": str(note)})
    return {"updated": True}
