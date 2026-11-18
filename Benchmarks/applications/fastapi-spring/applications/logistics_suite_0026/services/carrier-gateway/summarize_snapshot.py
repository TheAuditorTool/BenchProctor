# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/summarize_snapshot")
async def summarize_snapshot(request: Request):
    citation = request.headers.get('user-agent', '')
    requests.get(str(citation))
    return {"updated": True}
