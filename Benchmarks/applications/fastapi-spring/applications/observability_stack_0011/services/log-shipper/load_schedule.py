# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import socket


router = APIRouter()


@router.post("/load_schedule")
async def load_schedule(request: Request):
    caption = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    s = socket.create_connection((str(gauge), 80))
    s.close()
    return {"updated": True}
