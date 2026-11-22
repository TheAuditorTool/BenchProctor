# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/normalize_promotion")
async def normalize_promotion(request: Request):
    headline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    backorder = f'{headline!s}'
    Path('/var/app/data/' + str(backorder)).write_text('data')
    return {"updated": True}
