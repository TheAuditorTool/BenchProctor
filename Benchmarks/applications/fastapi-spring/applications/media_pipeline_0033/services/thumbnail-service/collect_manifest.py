# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/collect_manifest")
async def collect_manifest(request: Request):
    transcript = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(transcript)
    db.execute("SELECT * FROM users WHERE id = '" + str(rendition) + "'")
    return {"updated": True}
