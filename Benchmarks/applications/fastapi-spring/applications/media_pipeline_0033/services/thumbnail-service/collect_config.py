# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/collect_config")
async def collect_config(request: Request):
    transcript = (await request.body()).decode('utf-8')
    rendition = '{}'.format(transcript)
    requests.get(str(rendition))
    return {"updated": True}
