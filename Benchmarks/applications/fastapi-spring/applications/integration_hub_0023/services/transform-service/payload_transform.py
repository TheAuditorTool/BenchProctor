# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import unquote


router = APIRouter()


@router.post("/transform_payload")
async def transform_payload(request: Request):
    caption = request.cookies.get('session_token', '')
    handshake = unquote(caption)
    requests.post("http://connector-api:8080/InvokeConnector", json={"integrations_payload": str(handshake)})
    return {"updated": True}
