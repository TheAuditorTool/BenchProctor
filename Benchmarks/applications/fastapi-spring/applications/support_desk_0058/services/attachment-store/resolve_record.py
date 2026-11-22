# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/resolve_record")
async def resolve_record(request: Request):
    snippet = db.fetch_one('SELECT text FROM comments LIMIT 1')
    inquiry = f'{snippet!s}'
    Path('/var/app/data/' + str(inquiry)).write_text('data')
    return {"updated": True}
