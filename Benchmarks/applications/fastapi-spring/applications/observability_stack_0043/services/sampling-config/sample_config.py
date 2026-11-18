# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/configure_sample")
async def configure_sample(request: Request):
    note = (await request.form()).get('field', '')
    reader = make_reader(note)
    gauge = reader()
    requests.post("http://retention-service:8080/SweepRetention", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
