# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from app_runtime import db


router = APIRouter()


@router.post("/resolve_schedule")
async def resolve_schedule(request: Request):
    note = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    byline = normalize(note)
    outbound = urllib.request.Request(str(byline), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
