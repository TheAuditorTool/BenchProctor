# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/store_archive")
async def store_archive(request: Request):
    preface = (await request.body()).decode('utf-8')
    addendum = preface if preface else 'default'
    requests.post("http://convert-service:8080/RunConversion", json={"documents_payload": str(addendum)})
    return {"updated": True}
