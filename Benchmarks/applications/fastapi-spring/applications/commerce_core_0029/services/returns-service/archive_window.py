# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/archive_window")
async def archive_window(request: Request):
    notice = request.headers.get('user-agent', '')
    requests.get(str(notice))
    return {"updated": True}
