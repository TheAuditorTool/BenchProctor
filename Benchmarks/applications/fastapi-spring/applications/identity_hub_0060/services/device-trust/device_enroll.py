# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/enroll_device/{id}")
async def enroll_device(request: Request, id: str):
    paragraph = request.path_params.get('id', '')
    persona, _sep, _rest = str(paragraph).partition('\x00')
    requests.post("http://profile-api:8080/UpdateProfile", json={"identity_payload": str(persona)})
    return {"updated": True}
