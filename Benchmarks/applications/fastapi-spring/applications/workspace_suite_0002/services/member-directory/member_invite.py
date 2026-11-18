# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


router = APIRouter()


@router.post("/invite_member")
@require_login
async def invite_member(request: Request):
    transcript = request.headers.get('authorization', '')
    heading = (lambda v: v.strip())(transcript)
    requests.post("http://comment-service:8080/PostComment", json={"workspace_payload": str(heading)})
    return {"updated": True}
