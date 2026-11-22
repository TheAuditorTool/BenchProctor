# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/summarize_header")
async def summarize_header(request: Request):
    memo = db.fetch_one('SELECT text FROM comments LIMIT 1')
    backorder = f'{memo!s}'
    Path('/var/app/data/' + str(backorder)).write_text('data')
    return {"updated": True}
