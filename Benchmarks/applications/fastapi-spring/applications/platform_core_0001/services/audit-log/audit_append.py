# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/append_audit")
async def append_audit(request: Request):
    tagline = request.headers.get('authorization', '')
    reader = make_reader(tagline)
    persona = reader()
    requests.post("http://platform-api:8080/ProvisionTenant", json={"platform_payload": str(persona)})
    return {"updated": True}
