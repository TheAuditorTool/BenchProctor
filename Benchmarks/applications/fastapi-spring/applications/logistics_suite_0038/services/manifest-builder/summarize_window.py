# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/summarize_window")
async def summarize_window(request: Request):
    wording = request.headers.get('user-agent', '')
    requests.get(str(wording))
    return {"updated": True}
