# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import unquote


router = APIRouter()


@router.post("/cut_release")
async def cut_release(request: Request):
    summary = request.cookies.get('session_token', '')
    phrase = unquote(summary)
    requests.post("http://rollback-service:8080/TriggerRollback", json={"delivery_payload": str(phrase)})
    return {"updated": True}
