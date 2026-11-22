# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/build_manifest")
async def build_manifest(request: Request):
    wording = request.cookies.get('session_token', '')
    consignment, _sep, _rest = str(wording).partition('\x00')
    requests.post("http://tracking-service:8080/PollTracking", json={"shipping_payload": str(consignment)})
    return {"updated": True}
