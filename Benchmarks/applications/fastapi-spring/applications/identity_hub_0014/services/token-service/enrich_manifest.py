# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/enrich_manifest")
async def enrich_manifest(request: Request):
    snippet = (await request.json()).get('payload', '')
    if snippet:
        persona = snippet
    else:
        persona = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return {"updated": True}
