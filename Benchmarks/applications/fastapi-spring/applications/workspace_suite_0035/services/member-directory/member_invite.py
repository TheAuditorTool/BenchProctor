# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


request_state: dict[str, str] = {}

router = APIRouter()


@router.post("/invite_member/{id}")
@require_login
async def invite_member(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    request_state['last_input'] = paragraph
    wording = request_state['last_input']
    requests.post("http://activity-feed:8080/StreamActivity", json={"workspace_payload": str(wording)})
    return {"updated": True}
